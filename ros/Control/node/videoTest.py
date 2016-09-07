#!/usr/bin/env python

import urllib
import time

startTime = time.time()
endTime = time.time()
timeToRetrieveTime = endTime - startTime

startTime = time.time()
remoteImage = urllib.urlopen('http://robot:8080/?action=snapshot')
image = remoteImage.read()
localImage = open('/tmp/localImage.jpeg', 'w+')
localImage.write(image)
localImage.close()
endTime = time.time()

print "Once %4.3f" % (endTime - startTime - timeToRetrieveTime)
