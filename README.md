# LarmorSound v.1.0 Beta for Fabric Engine

Sound spectrum, samples and playback extension for [Fabric Engine](http://fabricengine.com/)

Author: Pier Paolo Ciarravano [http://www.larmor.com](http://www.larmor.com)

Watch the video demo: [LarmorSound on Windows Fabric Canvas and Maya https://vimeo.com/192639511](https://vimeo.com/192639511)
and [LarmorSound on Linux Fabric Canvas https://vimeo.com/190653588](https://vimeo.com/190653588)

**Notice:** the Beta version builds for Linux and Windows are expired on 31st March 2017. If you are interested in the new build please [contact me](http://www.larmor.com/menu/contact.html) for further information.

### Features:

* Extracts audio from all media file types: wav, mp3, mp4, mkv, mts, etc.
* Extracts all audio channels: mono, stereo, 5.1, etc.
* Spectrum output in time per each channel
* Audio energy in time per each channel
* Numeric samples output per channel
* Audio playback reproduction: Fabric Canvas play and stop buttons integrated using internal frame “heartbeat” sync
* Fabric Canvas, Maya and KL demo samples provided
* Windows and Linux versions (Mac OS X version available on January 2017)

[![LarmorSound - Fabric Maya Demo screenshot on Windows](https://github.com/ppciarravano/larmorsound/raw/master/doc/images/screenshot_canvas_maya_mid.png)](https://raw.githubusercontent.com/ppciarravano/larmorsound/master/doc/images/screenshot_canvas_maya.png)

[![LarmorSound - Fabric Canvas Demo screenshot on Linux](https://github.com/ppciarravano/larmorsound/raw/master/doc/images/screenshot_canvas_mid.png)](https://raw.githubusercontent.com/ppciarravano/larmorsound/master/doc/images/screenshot_canvas.png)

The extension is available for Windows and Linux x86_64, and it will be available for Max OS X on January 2017.

This project uses [LarmorSound API C++ v.1.0 Beta](https://github.com/ppciarravano/larmorsound-api).


### Installation for Fabric Engine 2.3.1 on Windows x86_64:

Extract the zip file in the directory specified by SET FABRIC_EXTS_PATH in your environment.bat e.g.:
```
C:\FabricEngine-2.3.1-Windows-x86_64\Exts\LarmorSound
```

### Installation for Fabric Engine 2.3.0 on Linux:

External required library dependencies for Linux build x86_64:
* SDL2 >= 2.0.4
* libavcodec >= 54.35.0 (part of ffmpeg-libs)
* libavformat >= 52.3.0 (part of ffmpeg-libs)
* libavutil >= 52.3.0 (part of ffmpeg-libs)
* libavresample >= 1.0.1 (part of ffmpeg-libs)

The extension uses [Aubio](http://aubio.org/) lib and the proprietary LarmorSoundAPI lib, both are deployed in the builds.

Download the tgz file for Linux [here](https://github.com/ppciarravano/larmorsound/blob/master/builds/linux/LarmorSound_1.0-Linux-x86_64.tgz).

Extract the tgz file in a directory specified by $FABRIC_EXTS_PATH e.g.:
```
/opt/FabricEngine-2.3.0-Linux-x86_64/Exts/LarmorSound
```
Add to LD_LIBRARY_PATH env variable the "LarmorSound/libs" path, e.g.:
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/FabricEngine-2.3.0-Linux-x86_64/Exts/LarmorSound/libs
```


### Run Samples:

Examples are at [https://github.com/ppciarravano/larmorsound/tree/master/samples](https://github.com/ppciarravano/larmorsound/tree/master/samples)

LarmorSound_DEMO_SpectrumViewer.canvas : example for Fabric Canvas.
LarmorSound_DEMO_plate_Canvas.canvas : example for Fabric Canvas.
LarmorSound_DEMO_plate_Maya_2017.mb : example for Autodesk Maya 2017.

For KL demo: edit the file LarmorSound_DEMO_stndln.kl replacing the media filename and execute:

```
kl LarmorSound_DEMO_stndln.kl
```

### License:

LarmorSound 1.0 Beta 2016: Extension for Fabric Engine

Copyright (c) 2016 Pier Paolo Ciarravano

[http://www.larmor.com](http://www.larmor.com)

All rights reserved.

LarmorSound is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

LarmorSound is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with LarmorSound. If not, see <http://www.gnu.org/licenses/>.

Licensees holding a valid commercial license may use this file in
accordance with the commercial license agreement provided with the
software.

---
