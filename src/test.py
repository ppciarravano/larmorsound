#
# Fabric Engine 2.3.0
# EDKObjects EDK Sample
#
# Copyright (c) 2010-2016, Fabric Software Inc. All rights reserved.
#

import os
if 'FABRIC_EXTS_PATH' in os.environ:
  os.environ['FABRIC_EXTS_PATH'] = os.pathsep.join(['.', os.environ['FABRIC_EXTS_PATH']])
else:
  os.environ['FABRIC_EXTS_PATH'] = '.'

#os.environ['FABRIC_EXTS_PATH'] = '.'
print "ECHO FABRIC_EXTS_PATH = " + os.environ['FABRIC_EXTS_PATH']

from time import sleep

import FabricEngine.Core as fabric
fabricClient = fabric.createClient();

fabricClient.loadExtension("LarmorSound")

lsObj = fabricClient.RT.types.LarmorSound.create("/home/larmor/DEVELOP/FabricSound_proj/samples/liz.mp3")
interfaceObj = fabricClient.RT.types.LarmorSound_Interface(lsObj)

numSamples = interfaceObj.getNumSamples("UInt32")
print numSamples.getSimpleType()
#print "Test LarmorSound numSamples = " + str(numSamples)
channelSample = interfaceObj.getChannelSample("Float32<>", 1)
print channelSample.getSimpleType()
print channelSample
#print "Test LarmorSound channelSample = " + str(channelSample)
#interfaceObj.initPlay("Boolean")
#interfaceObj.play("Boolean")

#sleep(10)

fabricClient.close()

