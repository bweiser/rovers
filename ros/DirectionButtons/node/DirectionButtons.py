#!/usr/bin/env python

# Copyright 2011 Adler Planetarium
# Created by Bill Mania and Mania Labs for Adler Planetarium
# bill@manialabs.us

import roslib ; roslib.load_manifest('DirectionButtons')

import usb.core
import rospy
import sys
from DirectionButtons.msg import *
from DirectionButtons.srv import Lamp
from InputEvents import InputEvents

class DirectionButtons():
    def __init__(self, name):

        self.name = name
        self.numberOfEvents = 0

        rospy.logdebug('Initializing DirectionButtons')
        self.initializeDirectionButtons()

        self.directionButtons = DirectionButton()
        rospy.logdebug('Registering as DirectionButton publisher')
        rospy.init_node('DirectionButtons', log_level = rospy.DEBUG)
        self.publisher = rospy.Publisher('directionButtons', DirectionButton)
        self.lampService = rospy.Service(
            'Lamps',
            Lamp,
            self.setLampState
            )

        rospy.loginfo('Initialization complete')

        return

    def initializeDirectionButtons(self):
        while True:
            try:
                self.device = usb.core.find(idVendor = 0x078b, idProduct = 0x0030)

                if self.device is None:
                    rospy.logwarn('Happ device not found. Trying again')
                    continue

                if self.device.is_kernel_driver_active(0):
                    self.device.detach_kernel_driver(0)
                    self.device.detach_kernel_driver(1)

                self.device.set_configuration()

                configurations = []
                interfaces = []
                endpoints = []
                for configuration in self.device:
                    configurations.append(configuration)
                    for interface in configuration:
                        interfaces.append(interface)
                        for endpoint in interface:
                            endpoints.append(endpoint)

                self.endpointAddress = endpoints[0].bEndpointAddress
                self.maxPacketSize = endpoints[0].wMaxPacketSize

                break

            except:
                rospy.logwarn('Unable to initialize Happ device')
                rospy.logwarn(' Type: %s' % (sys.exc_info()[0]))
                rospy.logwarn(' Value: %s' % (sys.exc_info()[1]))
                rospy.sleep(10.0)

        rospy.logdebug('Happ device initialized')

        self.inputLookup = {
            rospy.get_param('DirectionButtons/direction/forward') : InputEvents.FORWARD,
            rospy.get_param('DirectionButtons/direction/forwardRelease') : InputEvents.FORWARD_RELEASE,
            rospy.get_param('DirectionButtons/direction/backward') : InputEvents.BACKWARD,
            rospy.get_param('DirectionButtons/direction/backwardRelease') : InputEvents.BACKWARD_RELEASE,
            rospy.get_param('DirectionButtons/direction/left') : InputEvents.LEFT,
            rospy.get_param('DirectionButtons/direction/leftRelease') : InputEvents.LEFT_RELEASE,
            rospy.get_param('DirectionButtons/direction/right') : InputEvents.RIGHT,
            rospy.get_param('DirectionButtons/direction/rightRelease') : InputEvents.RIGHT_RELEASE,

            rospy.get_param('DirectionButtons/buttons/start') : InputEvents.START,
            rospy.get_param('DirectionButtons/buttons/startRelease') : InputEvents.START_RELEASE,
            rospy.get_param('DirectionButtons/buttons/top') : InputEvents.TOP,
            rospy.get_param('DirectionButtons/buttons/topRelease') : InputEvents.TOP_RELEASE,
            rospy.get_param('DirectionButtons/buttons/middle') : InputEvents.MIDDLE,
            rospy.get_param('DirectionButtons/buttons/middleRelease') : InputEvents.MIDDLE_RELEASE,
            rospy.get_param('DirectionButtons/buttons/bottom') : InputEvents.BOTTOM,
            rospy.get_param('DirectionButtons/buttons/bottomRelease') : InputEvents.BOTTOM_RELEASE
            }

        self.buttonLamps = {
            'StartLamp' : rospy.get_param('DirectionButtons/buttons/startLamp'),
            'TopLamp' : rospy.get_param('DirectionButtons/buttons/topLamp'),
            'MiddleLamp' : rospy.get_param('DirectionButtons/buttons/middleLamp'),
            'BottomLamp' : rospy.get_param('DirectionButtons/buttons/bottomLamp'),
            }

        return

    def readNextEvent(self):
        try:
            rospy.logdebug('Trying to read a button event')
            nextEvent = self.device.read(
                self.endpointAddress,
                self.maxPacketSize,
                timeout = 0
                )
            rospy.logdebug('Read a button event')

        except usb.core.USBError as e:
            rospy.logwarn('Happ device read error: %s') % (e.args[0])
            return InputEvents.UNKNOWN_EVENT

        nextEventKey = '%d,%d,%d,%d' % (
            nextEvent[0],
            nextEvent[1],
            nextEvent[2],
            nextEvent[3]
            )

        rospy.logdebug('Read event: %s' % (nextEventKey))
        self.numberOfEvents = self.numberOfEvents + 1
        if self.numberOfEvents > 100:
            rospy.logdebug('Number of jbserver events: %d' % (self.numberOfEvents))
            self.numberOfEvents = 0

        if self.inputLookup.has_key(nextEventKey):
            eventName = self.inputLookup[nextEventKey]
            if eventName in InputEvents.buttonReleases or eventName in InputEvents.joystickReleases:
                return InputEvents.GENERIC_RELEASE
            elif eventName in InputEvents.buttonPresses or eventName in InputEvents.joystickPresses:
                return eventName
            else:
                return InputEvents.UNKNOWN_EVENT
        else:
            return InputEvents.UNKNOWN_EVENT

    def setLampState(self, request):
        rospy.logdebug(
            "Lamp state change: %d" % (request.lampStates)
            )

        lampStateRequest = chr(8) + chr(request.lampStates) + chr(0)

        bmRequestType = 33             # host to device, class, interface
        bRequest = 9                   # SET_CONFIGURATION
        bytesSent = self.device.ctrl_transfer(
            bmRequestType,
            bRequest,
            0,
            0,
            lampStateRequest,
            None
            )

        if bytesSent == 3:
            return True
        else:
            return False

    def sendEvent(self, event):
        if self.client == None:
            rospy.logwarn('Reconnecting client')
            self.connectClient()

        try:
            self.client.send(event)
            self.client.send(InputEvents.eventTerminator)

        except:
            rospy.logwarn('send() failed, disconnecting')
            self.disconnectClient()

        return

    def processEvents(self):
        rospy.logdebug('Entering the processEvents loop')

        while not rospy.is_shutdown():
            nextEvent = self.readNextEvent()
            rospy.logdebug('Read event %s' % (nextEvent))
            self.directionButtons.buttonEvent = nextEvent
            self.publisher.publish(self.directionButtons)

        return

if __name__ == '__main__':

    dbInput = DirectionButtons('DBServer')
    
    dbInput.processEvents()

    rospy.loginfo('Stopping')

    sys.exit(0)
