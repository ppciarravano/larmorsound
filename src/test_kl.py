#
# Fabric Engine 2.3.0
# HelloWorld EDK Sample
#
# Copyright (c) 2010-2016, Fabric Software Inc. All rights reserved.
#

import os
if 'FABRIC_EXTS_PATH' in os.environ:
    os.environ['FABRIC_EXTS_PATH'] = os.pathsep.join(['.', os.environ['FABRIC_EXTS_PATH']])
else:
    os.environ['FABRIC_EXTS_PATH'] = '.'

from time import sleep

import FabricEngine.Core as fabric
fabricClient = fabric.createClient();

opSource = """
require LarmorSound;

operator entry(io String string) {
    report("KL: TEST");
    string = "This is a test";
    report("KL: " + string);

    //Object creation
    LarmorSound ls = LarmorSound(\"/home/larmor/DEVELOP/FabricSound_proj/samples/liz.mp3\");
    Float32 samples<> = ls.getChannelSample(0);
    report("SIZE: " + samples.size());
    for(Size i = 0; i < 100; i++) {
        report("ELEM: " + i + " --> " + samples[i]);
    }
    ls.initPlay();
    ls.play(13780352);

    while(ls.isPlaying()) {
        UInt32 position = ls.getPlayPosition();
        report("POSITION: " + ls.getPlayPosition());
        Float32 spectrum<> = ls.getChannelSpectrum(0, position);
        report("spectrum SIZE: " + spectrum.size());
        Float32 energy = ls.getChannelEnergy(0, position);
        report("ENERGY: " + energy);
        for(Size i = 0; i < 3; i++) {
            report("SPECT ELEM: " + i + " --> " + spectrum[i]);
        }
    }
}
"""
op = fabricClient.DG.createOperator("op")
op.setSourceCode(opSource)
op.setEntryPoint("entry")

b = fabricClient.DG.createBinding()
b.setOperator(op)
b.setParameterLayout(['self.string'])

node = fabricClient.DG.createNode("node")
node.addMember("string", "String")
node.bindings.append(b)
node.evaluate()
print "Python got: " + node.getData("string", 0)

fabricClient.close()
