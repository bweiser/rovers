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

onPayload = chr(8) + chr(int(sys.argv[1])) + chr(0)
offPayload = chr(8) + chr(0) + chr(0)

print "OFF"
bytesSent = device.ctrl_transfer(
    33,
    9,
    0,
    0,
    offPayload,
    None
    )

time.sleep(1.0)

print "ON"
bytesSent = device.ctrl_transfer(
    33,
    9,
    0,
    0,
    onPayload,
    None
    )

time.sleep(1.0)
