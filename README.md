# LarmorSound v.1.0 Beta for Fabric Engine

Sound spectrum, samples and playback extension for [Fabric Engine](http://fabricengine.com/)

Author: Pier Paolo Ciarravano [http://www.larmor.com](http://www.larmor.com)

[Watch the video demo: LarmorSound on Fabric Canvas https://vimeo.com/190653588](https://vimeo.com/190653588)


### Features:

* Extracts audio from all media file types: wav, mp3, mp4, mkv, mts, etc.
* Extracts all audio channels: mono, stereo, 5.1, etc.
* Spectrum output in time per each channel
* Audio energy in time per each channel
* Numeric samples output per channel
* Audio playback reproduction: Fabric Canvas play and stop buttons integrated using internal frame “heartbeat” sync
* Fabric Canvas and KL demo samples provided

[![LarmorSound - Fabric Canvas Demo screenshot](https://github.com/ppciarravano/larmorsound/raw/master/doc/images/screenshot_canvas_mid.png)](https://raw.githubusercontent.com/ppciarravano/larmorsound/master/doc/images/screenshot_canvas.png)

The extension is now just available for Linux x86_64, and it will be soon available for Max OS X and Windows.


### Installation for Fabric Engine 2.3.0 on Linux:

External required library dependencies for Linux build x86_64:
* SDL2 >= 2.0.4
* libavcodec >= 54.35.0
* libavformat >= 52.3.0
* libavutil >= 52.3.0
* libavresample >= 1.0.1

Download the tgz file for Linux [here](https://github.com/ppciarravano/larmorsound/blob/master/builds/linux/LarmorSound_1.0-Linux-x86_64.tgz).

Extract the tgz file in the directory specified by $FABRIC_EXTS_PATH e.g.:
```
/opt/FabricEngine-2.3.0-Linux-x86_64/Exts/LarmorSound
```
Add to LD_LIBRARY_PATH env variable the "LarmorSound/libs" path, e.g.:
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/FabricEngine-2.3.0-Linux-x86_64/Exts/LarmorSound/libs
```


### Run Samples:

Open the file LarmorSound_DEMO_SpectrumViewer.canvas from Fabric Canvas.

For KL demo: edit the file LarmorSound_DEMO_stndln.kl replacing the media filename and execute:

```
kl LarmorSound_DEMO_stndln.kl
```

### License:

Copyright (c) 2016 Pier Paolo Ciarravano
[http://www.larmor.com](http://www.larmor.com)
All rights reserved.

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

---
