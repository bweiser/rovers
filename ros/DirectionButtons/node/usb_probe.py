#!/usr/bin/env python

"""
 bmRequestType =
    bit 7 - host to device
    bits 5-6 - class
    bits 0-4 - interface

 bRequest =
    SET_CONFIGURATION (9)

 return value = 3
"""

import sys
import time
import usb.core

device = usb.core.find(idVendor = 0x078b, idProduct = 0x0030)

try:
    if device.is_kernel_driver_active(0):
        device.detach_kernel_driver(0)
        device.detach_kernel_driver(1)

    device.set_configuration()
except:
    print "Unable to setup the device"
    sys.exit(1)

onPayload = chr(8) + chr(127) + chr(0)
offPayload = chr(8) + chr(0) + chr(0)

#for bmRequestType in range(128):
#    for bRequest in [1,3,5,7,9,11]:
#        try:
#            bytesSent = device.ctrl_transfer(
#                bmRequestType,
#                bRequest,
#                0,
#                0,
#                payload,
#                None
#                )
#            print bmRequestType, bRequest, bytesSent
#            time.sleep(0.1)
#        except:
#            pass

while True:
    print "ON"
    bytesSent = device.ctrl_transfer(
        33,
        9,
        0,
        0,
        onPayload,
        None
        )

    time.sleep(2.0)

    print "OFF"
    bytesSent = device.ctrl_transfer(
        33,
        9,
        0,
        0,
        offPayload,
        None
        )

    time.sleep(2.0)

    
