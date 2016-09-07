
# Copyright 2011 Adler Planetarium
# Created by Bill Mania and Mania Labs for Adler Planetarium
# bill@manialabs.us

import roslib ; roslib.load_manifest('Control')
import rospy

import time

class UserInterfaceMessages():
    def __init__(self, name):
        self.name = name

        self.fieldDelimiter = rospy.get_param('Control/ui/fieldDelimiter')
        self.messageDelimiter = rospy.get_param('Control/ui/messageDelimiter')  + '\r\n'
        self.messageDelimiterLength = len(self.messageDelimiter)
        self.sequenceNumber = 0

        rospy.logdebug('UserInterfaceMessages initialized')
        
        return

    def uiMessage(self, payloadLength, payload):
        message = "%d%s%d%s%d%s%s%s" % (self.sequenceNumber,
                self.fieldDelimiter,
                int(time.time()),
                self.fieldDelimiter,
                payloadLength + self.messageDelimiterLength,
                self.fieldDelimiter,
                payload,
                self.messageDelimiter
                )

        self.sequenceNumber = self.sequenceNumber + 1

        return message
        
    def ackMessage(self, version):
        payload = 'ACK%s%d' % (self.fieldDelimiter,
                int(version)
                )
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def startMessage(self,
            roverSerial,
            roverIp,
            batteryChargeLevel
            ):

        payload = 'START%s%s%s%s%s%3.1f' % (self.fieldDelimiter,
                roverSerial,
                self.fieldDelimiter,
                roverIp,
                self.fieldDelimiter,
                batteryChargeLevel
                )
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def stateMessage(self,
            batteryChargeLevel,
            goalReached,
            goalProximityReached,
            sessionSecondsRemaining
            ):

        payload = "STATE%s%d%s%s%s%s%s%d" % (self.fieldDelimiter,
                batteryChargeLevel,
                self.fieldDelimiter,
                goalReached,
                self.fieldDelimiter,
                goalProximityReached,
                self.fieldDelimiter,
                sessionSecondsRemaining
                )
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def buttonMessage(self, whichButton):

        payload = "BUTTON%s%s" % (self.fieldDelimiter,
                whichButton
                )
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def doneMessage(self, timeToFindAll):

        payload = "DONE%s%d" % (self.fieldDelimiter,
                timeToFindAll
                )
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def expireMessage(self,
            periodWhichExpired,
            delaySeconds):

        payload = "EXPIRE%s%s%s%d" % (
            self.fieldDelimiter,
            periodWhichExpired,
            self.fieldDelimiter,
            delaySeconds)
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def nofuelMessage(self,
            roverSerial):

        payload = "NOFUEL%s%s" % (self.fieldDelimiter, roverSerial)
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

    def videoMessage(self,
            frameJpeg):
        payload = "VIDEO%s%s" % (self.fieldDelimiter,
                frameJpeg
                )
        payloadLength = len(payload)
        
        return self.uiMessage(payloadLength, payload)

    def errorMessage(self,
            errorText):

        payload = "ERROR%s%s" % (self.fieldDelimiter, errorText)
        payloadLength = len(payload)

        return self.uiMessage(payloadLength, payload)

