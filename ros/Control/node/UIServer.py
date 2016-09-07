
# Copyright 2011 Adler Planetarium
# Created by Bill Mania and Mania Labs for Adler Planetarium
# bill@manialabs.us

import roslib ; roslib.load_manifest('Control')
import rospy

import sys
import socket
from UserInterfaceMessages import *

class UIServer():
    def __init__(self, name):

        self.name = name
        self.uiMessages = UserInterfaceMessages(self.name)

        self.connection = None
        self.clientDetails = None
        self.server = None

        self.connectClient()

        return

    def connectClient(self):
        if self.server != None:
            rospy.logwarn('Already connected')
            return

        self.listenPort = rospy.get_param('Control/ui/portNumber')
        rospy.logdebug('UIServer waiting for UI client to connect, listening on 0.0.0.0:%d' % (
                self.listenPort
                )
                )

        self.server = socket.socket(socket.AF_INET,
                socket.SOCK_STREAM
                )
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', self.listenPort))
        self.server.listen(1)
        self.connection, self.clientDetails = self.server.accept()

        self.sendMessage(
                self.uiMessages.ackMessage(
                        rospy.get_param('Control/ui/versionNumber')
                        )
                )

        rospy.loginfo('%s connected from port %d' % (self.clientDetails[0],
                self.clientDetails[1]))

        return

    def disconnectClient(self):
        try:
            self.connection.close()
            self.server.close()

        except:
            pass

        self.connection = None
        self.server = None
        self.clientDetails = None

        return

    def sendMessage(self, message):
        if self.connection == None:
            rospy.logwarn('Reconnecting client')
            self.disconnectClient()
            self.connectClient()

        try:
            self.connection.send(message)

        except:
            exceptionType, exceptionValue = sys.exc_info()[:2]
            rospy.logwarn('UIServer.sendMessage() failed, reconnecting but tossing message')
            rospy.logwarn(' Type: %s, Value: %s' %
                    (exceptionType,
                    exceptionValue)
                    )
            self.disconnectClient()
            self.connectClient()

        return

