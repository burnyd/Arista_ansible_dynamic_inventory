#Please copy the following files from CVP into you're python libraries 
#/usr/lib/python2.7/site-packages/cvp.py 
#/usr/lib/python2.7/site-packages/cvpServices.py 
#/usr/lib/python2.7/site-packages/cvpConfigParser.py 
#/usr/lib/python2.7/site-packages/errorCodes.py 

#!/usr/bin/env python

import cvp
import json
from jsonrpclib import Server
import sys

host = '192.168.0.202'
server = cvp.Cvp(host)
server.authenticate('arista','arista')

#This is a function to find all devices within cvp
def findalldevices():
    deviceList = []
    for device in server.getDevices():
        deviceName = device.fqdn #calls the cvp api for device.fqdn
        deviceList.append(deviceName) #appens to the list each item
        dynamicList = [str(i) for i in deviceList]
    return dynamicList

dynamic = findalldevices()

def dynamic_inventory():
    print  {
            'arista': {
                'hosts': dynamic,
                'vars': {
                    'ansible_connection': "local",
                    'username': 'arista',
                    'password': 'arista',
                    'transport': 'cli',
		    'use_ssl': 'true',
                }
	}
 }


dynamic_inventory()
