#!/usr/bin/env python

# Copyright 2011 Adler Planetarium
# Created by Bill Mania and Mania Labs for Adler Planetarium
# bill@manialabs.us

import roslib ; roslib.load_manifest('Control')
import rospy

from RfidReader.msg import Rfid
from DirectionButtons.msg import DirectionButton
from DirectionButtons.srv import Lamp
from DriveMotors.srv import Move
from RoverState.msg import Battery, Range

from Mail import MailTransport, MailMessage

import sys
import urllib

from UIServer import *
from InputEvents import InputEvents

serverName = 'control'
sessionStarted = False
motorService = None
lampService = None
lampStates = 0
directionButtonsSubscriber = None
batteryInfoSubscriber = None
rfidSubscriber = None
topButtonEnabled = False
middleButtonEnabled = False
bottomButtonEnabled = False
startButtonEnabled = False
chargeLevel = 100
driveSpeed = 50
turnSpeed = 40
batteryDepleted = False
serialNumber = 'Unknown'
goalsFound = []

def handleVideoMessage(ui):
    remoteImage = urllib.urlopen('http://rover1:8080/?action=snapshot')
    image = remoteImage.read()
    remoteImage.close()

    ui.sendMessage(
        uiMessages.videoMessage(
            image
            )
        )

    return

def notifyOperator(message, subject):
    try:
        nofuelMessage = MailMessage(
            message,
            subject,
            rospy.get_param('Control/mail/fromAddress'),
            rospy.get_param('Control/mail/toAddressList')
            )
        mta = MailTransport(
            rospy.get_param('Control/mail/relayServer'),
            rospy.get_param('Control/mail/userName'),
            rospy.get_param('Control/mail/password')
            )
        mta.sendMessage(nofuelMessage)
        mta.done()

    except:
        rospy.logwarn('Unable to notify operator')

    return

def callLampService(whichLamp, turnItOn):
    global lampStates

    if turnItOn:
        newLampStates = lampStates | whichLamp
    else:
        newLampStates = lampStates & (~ whichLamp)

    try:
        if lampService(newLampStates):
            lampStates = newLampStates
        else:
            rospy.logwarn('Call to lampService failed')

    except:
        rospy.logwarn('Call to lampService excepted')
        rospy.logwarn(' Type: %s' % (sys.exc_info()[0]))
        rospy.logwarn(' Value: %s' % (sys.exc_info()[1]))

    return

def callMotorService(left, right, duration, acceleration):
    global motorService, sessionStarted, startButtonEnabled
    global directionButtonsSubscriber, batteryInfoSubscriber, rfidSubscriber

    try:
        motorService(left, right, duration, acceleration)

    except rospy.ServiceException:
        sessionStarted = False
        startButtonEnabled = False
        callLampService(
            rospy.get_param('DirectionButtons/buttons/startLamp'),
            False
            )
        rospy.logwarn('Call to motorService failed. Re-initializing')
        try:
            motorService.close()
        except:
            rospy.logwarn('motorService.close() failed')
        
        directionButtonsSubscriber.unregister()
        batteryInfoSubscriber.unregister()
        rfidSubscriber.unregister()

        ui.sendMessage(uiMessages.nofuelMessage(serialNumber)) 
        notifyOperator('Replace with charged rover', 'Rover battery depleted')

        rospy.logdebug('Waiting for DriveMotors to resume')
        while True:
            try:
                rospy.wait_for_service('DriveMotors', timeout = 600)
                break

            except:
                rospy.logwarn('Timed out waiting for replacement rover. Trying again')
                notifyOperator('Will wait another 600 seconds', 'Timeout waiting for new rover')

        motorService = rospy.ServiceProxy('DriveMotors', Move, persistent = True)
        directionButtonsSubscriber = rospy.Subscriber('directionButtons', DirectionButton, buttonEvent)
        batteryInfoSubscriber = rospy.Subscriber('batteryInfo', Battery, batteryEvent)
        rfidSubscriber = rospy.Subscriber('rfid', Rfid, rfidEvent)

        startButtonEnabled = True
        callLampService(
            rospy.get_param('DirectionButtons/buttons/startLamp'),
            True
            )
        rospy.logdebug('DriveMotors resumed')

    return

def batteryEvent(batteryInfo):
    global chargeLevel, batteryDepleted

    chargeLevel = batteryInfo.batteryVoltagePercentage
    batteryDepleted = batteryInfo.depleted
    if batteryDepleted:
        ui.sendMessage(uiMessages.nofuelMessage(serialNumber)) 
        notifyOperator('Need charged rover', 'Rover battery depleted')

    return
    
def buttonEvent(whichButton):

    global sessionStarted, startButtonEnabled, topButtonEnabled, middleButtonEnabled, bottomButtonEnabled

    rospy.logdebug('buttonEvent() called with %s' % (
            whichButton.buttonEvent
            ))

    if sessionStarted:
        rospy.logdebug('sessionStarted')

    if whichButton.buttonEvent in InputEvents.joystickPresses and sessionStarted:
        rospy.logdebug('joystickPresses')
        if whichButton.buttonEvent == InputEvents.FORWARD:
            response = callMotorService(driveSpeed, driveSpeed, 0, 50)
        elif whichButton.buttonEvent == InputEvents.BACKWARD:
            response = callMotorService(-(driveSpeed), -(driveSpeed), 0, 50)
        elif whichButton.buttonEvent == InputEvents.LEFT:
            response = callMotorService(-(turnSpeed), (turnSpeed), 0, 50)
        elif whichButton.buttonEvent == InputEvents.RIGHT:
            response = callMotorService((turnSpeed), -(turnSpeed), 0, 50)
        else:
            response = callMotorService(0, 0, 0, 50)

    elif whichButton.buttonEvent in InputEvents.joystickReleases and sessionStarted:
        rospy.logdebug('joystickReleases')
        response = callMotorService(0, 0, 0, 50)

    elif whichButton.buttonEvent in InputEvents.buttonPresses:
        rospy.logdebug('buttonPresses')
        if startButtonEnabled:
            rospy.logdebug('startButtonEnabled')
        if topButtonEnabled:
            rospy.logdebug('topButtonEnabled')
        if middleButtonEnabled:
            rospy.logdebug('middleButtonEnabled')
        if bottomButtonEnabled:
            rospy.logdebug('bottomButtonEnabled')

        if whichButton.buttonEvent == InputEvents.START and startButtonEnabled:
            sessionStarted = True
        elif whichButton.buttonEvent == InputEvents.TOP and topButtonEnabled:
            ui.sendMessage(uiMessages.buttonMessage(whichButton.buttonEvent))
            topButtonEnabled = False
            callLampService(
                rospy.get_param('DirectionButtons/buttons/topLamp'),
                False
                )
        elif whichButton.buttonEvent == InputEvents.MIDDLE and middleButtonEnabled:
            ui.sendMessage(uiMessages.buttonMessage(whichButton.buttonEvent))
            middleButtonEnabled = False
            callLampService(
                rospy.get_param('DirectionButtons/buttons/middleLamp'),
                False
                )
        elif whichButton.buttonEvent == InputEvents.BOTTOM and bottomButtonEnabled:
            ui.sendMessage(uiMessages.buttonMessage(whichButton.buttonEvent))
            bottomButtonEnabled = False
            callLampService(
                rospy.get_param('DirectionButtons/buttons/bottomLamp'),
                False
                )
            
    return

def rfidEvent(rfid):
    global goalsFound, topButtonEnabled, middleButtonEnabled, bottomButtonEnabled

    rospy.logdebug('Received RFID: %s' % (rfid.rfidTag))

    if rfid.goalOrProximity == 'Goal':
        goalReached = rfid.rfidTag
        if goalReached not in goalsFound:
            goalsFound.append(goalReached)
        goalProximityReached = ''
        if goalReached == InputEvents.TOP_RELEASE:
            topButtonEnabled = True
            callLampService(
                rospy.get_param('DirectionButtons/buttons/topLamp'),
                True
                )
        elif goalReached == InputEvents.MIDDLE_RELEASE:
            middleButtonEnabled = True
            callLampService(
                rospy.get_param('DirectionButtons/buttons/middleLamp'),
                True
                )
        elif goalReached == InputEvents.BOTTOM_RELEASE:
            bottomButtonEnabled = True
            callLampService(
                rospy.get_param('DirectionButtons/buttons/bottomLamp'),
                True
                )
    else:
        goalProximityReached = rfid.rfidTag
        goalReached = ''
        
    ui.sendMessage(
        uiMessages.stateMessage(
            chargeLevel,
            goalReached,
            goalProximityReached,
            sessionSecondsLeft
            )
        )

    if len(goalsFound) >= 3:
        ui.sendMessage(
            uiMessages.doneMessage(
                rospy.get_param('Control/timers/sessionSeconds') - sessionSecondsLeft
                )
            )
        goalsFound = []

    return

def mainControlLoop(ui):

    global sessionStarted, startButtonEnabled, motorService, lampService
    global directionButtonsSubscriber, batteryInfoSubscriber, rfidSubscriber

    directionButtonsSubscriber = rospy.Subscriber('directionButtons', DirectionButton, buttonEvent)
    batteryInfoSubscriber = rospy.Subscriber('batteryInfo', Battery, batteryEvent)
    rfidSubscriber = rospy.Subscriber('rfid', Rfid, rfidEvent)
    rospy.logdebug('Waiting for DriveMotors service to become available')
    while True:
        try:
            rospy.wait_for_service('DriveMotors', timeout = 300)
            break

        except:
            rospy.logwarn('Timed out waiting for DriveMotors service. Trying again')

    motorService = rospy.ServiceProxy('DriveMotors', Move, persistent = True)
    rospy.logdebug('DriveMotors service is available and connected')

    rospy.logdebug('Waiting for Lamps service to become available')
    while True:
        try:
            rospy.wait_for_service('Lamps', timeout = 300)
            break

        except:
            rospy.logwarn('Timed out waiting for Lamps service. Trying again')

    lampService = rospy.ServiceProxy('Lamps', Lamp, persistent = True)
    rospy.logdebug('Lamps service is available and connected')

    callLampService(
        rospy.get_param('DirectionButtons/buttons/startLamp'),
        False
        )
    callLampService(
        rospy.get_param('DirectionButtons/buttons/topLamp'),
        False
        )
    callLampService(
        rospy.get_param('DirectionButtons/buttons/middleLamp'),
        False
        )
    callLampService(
        rospy.get_param('DirectionButtons/buttons/bottomLamp'),
        False
        )

    serialNumber = rospy.get_param('Control/rover/serialNumber')
    ipAddress = rospy.get_param('Control/rover/ipAddress')

    while not rospy.is_shutdown():
        callLampService(
            rospy.get_param('DirectionButtons/buttons/startLamp'),
            True
            )
        startButtonEnabled = True

        while not sessionStarted:
            rospy.sleep(1.0)

        callLampService(
            rospy.get_param('DirectionButtons/buttons/startLamp'),
            False
            )
        startButtonEnabled = False

        ui.sendMessage(uiMessages.startMessage(serialNumber, ipAddress, chargeLevel)) 

        endOfSession = rospy.get_time() + rospy.get_param('Control/timers/sessionSeconds')

        while rospy.get_time() < endOfSession and not rospy.is_shutdown():
            sessionSecondsLeft = int(endOfSession - rospy.get_time())
        
            ui.sendMessage(
                uiMessages.stateMessage(
                    chargeLevel,
                    '',
                    '',
                    sessionSecondsLeft
                    )
                )

            rospy.sleep(1.0)
        
        if rospy.get_time() >= endOfSession:
            sessionStarted = False
            response = callMotorService(0, 0, 0, 50)
            rospy.logdebug('Session expired')
            delaySeconds = rospy.get_param('Control/timers/interSessionDelaySeconds')
            ui.sendMessage(uiMessages.expireMessage('Play', delaySeconds)) 
            rospy.sleep(delaySeconds)
            ui.sendMessage(uiMessages.expireMessage('Intermission', 0)) 

if __name__ == '__main__':

    rospy.init_node('Control', log_level = rospy.DEBUG)
    rospy.loginfo('%s starting' % (serverName))

    ui = UIServer(serverName)
    rospy.logdebug('UIServer connected')

    uiMessages = ui.uiMessages

    mainControlLoop(ui)

    rospy.logwarn('Stopping')

    sys.exit(0)
