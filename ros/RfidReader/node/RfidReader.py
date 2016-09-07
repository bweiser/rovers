#!/usr/bin/env python

# Copyright 2011 Adler Planetarium
# Created by Bill Mania and Mania Labs for Adler Planetarium
# bill@manialabs.us

import roslib; roslib.load_manifest('RfidReader')

import rospy
from RfidReader.msg import Rfid
import sys
import serial

class RfidReader():
    def __init__(self):

        rospy.logdebug('Initializing RfidReader')

        while True:
            try:
                self.rfidDevice = serial.Serial(
                    port = rospy.get_param('RfidReader/serial/port'),
                    baudrate = rospy.get_param('RfidReader/serial/speed'),
                    timeout = rospy.get_param('RfidReader/serial/timeout') 
                    )
                self.rfidDevice.setRTS(level = True)
                self.rfidDevice.setDTR(level = True)
                break
    
            except serial.SerialException as e:
                rospy.logwarn('Unable to open %s' % (rospy.get_param('RfidReader/serial/port')))
                rospy.sleep(15.0)

            except serial.SerialTimeoutException as e:
                rospy.logwarn('Timeout waiting to open %s' % (rospy.get_param('RfidReader/serial/port')))
                rospy.sleep(15.0)

        self.topGoalRfid = ''
        self.topGoalName = ''
        self.topGoalRfidList = []
        self.topGoalProximityName = ''
        self.middleGoalRfid = ''
        self.middleGoalName = ''
        self.middleGoalRfidList = []
        self.middleGoalProximityName = ''
        self.bottomGoalRfid = ''
        self.bottomGoalName = ''
        self.bottomGoalRfidList = []
        self.bottomGoalProximityName = ''
        self.unknownRfid = ''

        rospy.logdebug("Building lists of RFID tags")
        self.initializeRfidLists()

        self.rfid = Rfid()
        self.rfid.rfidTag = ''
        self.rfid.goalOrProximity = 'Neither'
        rospy.logdebug("Registering as Rfid publisher")
        rospy.init_node('RfidReader', log_level = rospy.DEBUG)
        self.publisher = rospy.Publisher('rfid', Rfid)

        rospy.loginfo('Initialization complete')

    def sendRfidCommand(self, command):
        rospy.logdebug('Sending command: %s' % (command))
        self.rfidDevice.write('%s\r' % (command))

        return

    def readRfidResponse(self):
        response = ''
        characterRead = self.rfidDevice.read(1)
        while characterRead != '>':
            if characterRead not in [ '\r', '\n' ]:
                response = response + characterRead
            characterRead = self.rfidDevice.read(1)

        rospy.logdebug('Read <%s> from RFID' % (response))

        if response[6:] == self.topGoalRfid:
            return self.topGoalName, 'Goal'
        if response[6:] in self.topGoalRfidList:
            return self.topGoalProximityName, 'Proximity'
        if response[6:] == self.middleGoalRfid:
            return self.middleGoalName, 'Goal'
        if response[6:] in self.middleGoalRfidList:
            return self.middleGoalProximityName, 'Proximity'
        if response[6:] == self.bottomGoalRfid:
            return self.bottomGoalName, 'Goal'
        if response[6:] in self.bottomGoalRfidList:
            return self.bottomGoalProximityName, 'Proximity'

        return self.unknownRfid, 'Neither'

    def initializeRfidLists(self):
        self.sendRfidCommand('ctl')
        self.readRfidResponse()

        self.unknownRfid = rospy.get_param('RfidReader/tags/unknownRFID')

        self.topGoalRfid = rospy.get_param('RfidReader/tags/topGoal/RFID')
        self.topGoalName = rospy.get_param('RfidReader/tags/topGoal/name')
        self.topGoalProximityName = rospy.get_param('RfidReader/tags/topGoal/proximityName')
        self.sendRfidCommand('st %s' % (self.topGoalRfid))
        self.readRfidResponse()

        for rfid in rospy.get_param('RfidReader/tags/topGoal/proximityList').split(','):
            self.topGoalRfidList.append(rfid)
            self.sendRfidCommand('st %s' % (rfid))
            self.readRfidResponse()

        self.middleGoalRfid = rospy.get_param('RfidReader/tags/middleGoal/RFID')
        self.middleGoalName = rospy.get_param('RfidReader/tags/middleGoal/name')
        self.middleGoalProximityName = rospy.get_param('RfidReader/tags/middleGoal/proximityName')
        self.sendRfidCommand('st %s' % (self.middleGoalRfid))
        self.readRfidResponse()

        for rfid in rospy.get_param('RfidReader/tags/middleGoal/proximityList').split(','):
            self.middleGoalRfidList.append(rfid)
            self.sendRfidCommand('st %s' % (rfid))
            self.readRfidResponse()

        self.bottomGoalRfid = rospy.get_param('RfidReader/tags/bottomGoal/RFID')
        self.bottomGoalName = rospy.get_param('RfidReader/tags/bottomGoal/name')
        self.bottomGoalProximityName = rospy.get_param('RfidReader/tags/bottomGoal/proximityName')
        self.sendRfidCommand('st %s' % (self.bottomGoalRfid))
        self.readRfidResponse()

        for rfid in rospy.get_param('RfidReader/tags/bottomGoal/proximityList').split(','):
            self.bottomGoalRfidList.append(rfid)
            self.sendRfidCommand('st %s' % (rfid))
            self.readRfidResponse()

        return

    def processRfidEvents(self):
        while not rospy.is_shutdown():
            tagName, tagType = self.readRfidResponse()
            rospy.logdebug('Read tag %s with type %s' % (tagName, tagType))
            self.rfid.rfidTag = tagName
            self.rfid.goalOrProximity = tagType
            self.publisher.publish(self.rfid)

        return

if __name__ == '__main__':

    rfidEvents = RfidReader()
    
    rospy.logdebug('Entering processing loop')
    rfidEvents.processRfidEvents()

    rospy.logwarn('Stopping')

    sys.exit(0)
