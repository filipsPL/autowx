# :warning: There is a new, improved, rewriten, enchanced version of this tool called *autowx2* which is available here: https://github.com/filipsPL/autowx2/

Here: https://github.com/filipsPL/autowx2/

This code is no longer maintaned.

# About this fork

:warning: this is fork from cyber-atomus/autowx, modified to fit my needs.

## Main changes:
- changed directory structure (minor)
- auto calibration of the dongle
- acquiring APRS singnals instead of sleeping
- may not work as expected.

## Additional requirements:
- kalibrate (for calibration): install [one of the modern forks](https://github.com/steve-m/kalibrate-rtl/network)
- gopow (for heatmap plots): https://github.com/dhogborg/rtl-gopow/releases
- pymultimonaprs

# Orginal readme part:

autowx: This is a rewrite of rtlsdr-automated-wxsat-capture.

Automate Recording of Low Earth Orbit NOAA & Meteor Weather Satellites
License:  MIT

assumptions: Linux-based computer, rtl-sdr usb dongle, stationary antenna, experienced python & Linux user

goal:  record wav files for later processing, postprocess wav file, generate image, send images using SCP. Decode Meteor M2 images.

prerequistes:  working rtl-sdr, nsat/pypredict libraries, basic python libraries (subprocess, os, re, sys, time, datetime), tledraw uses matplotlib+pylab+numpy, sox, gnuradio, XvFB, WINE, Oleg LRPT Offline decoder, setup noaa.py/pypredict.py, setup all scripts

NO WARRANTY:  ALL USE IS AT THE RISK OF THE USER.  These are scripts I use for hobbyist purposes.  There may
be pre-requisites or system configuration differences which you will need to resolve in order to make use of these scripts in your project.  To do so requires patience and and, quite often, previous experience programming python 
and/or maintaining Linux-based rtl-sdr software.

This program also uses software which has no clear licensing information (wxtoimg).

##FILES

###LICENSE 
MIT 

###BASIC usage info
Prerequisites:

nsat/pypredict package:

git clone https://github.com/nsat/pypredict.git

cd pypredict

sudo apt-get install python-dev

sudo python setup.py install


As for wxtoimg I strongly recomment grabbing .tar.gz package and unpacking it to your /usr/local/ dir. Packages are provided on wxtoimg website.

NEW: Oleg's LRPT Offline Decoder

NEW: GNURADIO - record QPSK stream (Meteor M2)

NEW: WINE - for running Oleg's LRPT offline decoder (Meteor M2)

NEW: Xvfb - for running wine/LRPT decoder in Virtual Framebuffer (Meteor M2)

Installing autowx:
git pull https://github.com/cyber-atomus/autowx.git

You MUST create different folder for Meteor M2 images/logs and ini files. Then create a symlink to it in ~/.wine/dosdevices/X: (where X is desired virtual disk drive) and copy LRPT decoder as rgb.exe and mono.exe (important). Now edit the file meteor_qpsk and change DRIVE_LETTER to your drive letter and DIRECTORY (must be in subdir). (rgb|mono).ini must be in the same dir as (rgb|mono).exe, otherwise it won't decode pictures automatically and process will stall.
If you wish not to decode automatically, set meteorDecode to 'no' in noaa.py. 

###noaa.py
This is the main python script.  It will calculate the time of the next pass for recording.  It expects to call rtl_fm to do the recording and sox to convert the file to .wav. It can create spectrogram of the pass using sox (not the RTL_POWER!).
Station options are set in the script.

####A few words about the options.
* systemDir - directory where all scripts reside
* satellites - this is a list of satellites you want to capture, this needs to be the same name as in TLE file.
* freqs - frequencies of centre of the APT signal. Doesn't really matter for meteor as it's defined in GNURadio block
* dongleGain - set this to the desired gain of the dongle, leave "0" if you want AGC.
* dongleShift - set this to the dongle PPM shift, can be negative.
* dongleIndex - set this to the index of your dongle, of you have only one - leave it unchanged.
* sample - "sample rate", option "-s" for rtl_fm - this is the width of the recorded signal. Please keep in mind that APT is 34kHz but you should include few kHz for doppler shift. This will change when the doppler tool is used.
* wavrate - sample rate of the WAV file used to generate JPEGs. Should be 11025.

####Station options (QTH)
* stationLat - Station latitude - postivie for North, negative for South
* stationLon - Station longtitude - positive for West, negative for East
* stationAlt - Station altitude
* tleDir - Directory where to look for TLE files, default /tmp (as in update-keps.sh)
* tleFile - TLE filename (as in update-keps.sh)
* minElev - Minimal elevation for prediction and record
* minElevMeteor - Minimal elevation for Meteor - must be defined
* decodeMeteor - Should we decode meteor files?
* removeRaws - should we remove RAW wave files (after transcoding to 11kHz)

####Directories: directories used for misc. files

* recdir - this is a directory containing RAW and WAV files.
* specdir - this is a directory holding spectrogram files created from the pass (PNG).
* imgdir - where to put output JPG images.
* mapDir - directory for autogenerated maps (these are generated using wxmap using values from predict.qth).

####WXtoIMG options
* wxAddOverlay - Should the script generate images with map overlay?
* wxEnhCreate - Create NOAA enhancements? Without this setting only raw wxtoimg decode would be created
* wxEnhList - List of NOAA enhancements script should create, look at wxtoimg documentation which enhancements are supported
* wxQuietOutput - Silent output, everything's logged
* wxDecodeAll - the same as -A option in wxtoimg - decode everything, including noise
* wxJPEGQuality - quality of JPEG files
* wxAddTextOverlay - if the script should add custom overlay text
* wxOverlayText - Custom text
* wxOverlayOffsetX - offset map on image, negative moves map left, positive moves map right
* wxOverlayOffsetY - offset map on image, negative moves map up, positive moves map right

#####Other options
* createSpectro - creates sox spectrogram, useful for debugging 
* SCP_USER - user name for SCP-ing images and logs
* SCP_HOST - hostname for SCP-ing images
* SCP_DIR - remote directory to copy images/logs
* LOG_SCP - if the script should copy logs to remote server
* IMG_SCP - if the script should copy images to remote server
* loggingEnable - of you need noaa.py logs saved, set this to "yes"
* logFileName - log file name, including directory
* scriptPID - where to put script PID file 
* statusFile - status file name, for simple remote status (few TODOS)
* sfpgLink - if you use SFPG script it creates symlink for latest image previev, normally set it to something other than 'y', 'yes' or '1'


###pypredict.py
This is a short python module for extracting the AOS/LOS times
of the next pass for a specified satellite.  It uses nsat/pypredict for satellite prediction. Few settings:
* opoznienie - recording delay in seconds to prevent recording low elevation noise
* skrocenie - short the recording by XX seconds to prevent recording low elevation noise

###tletest.py
Small script for quick dumping nearest passes, few settings:
* qth() - as in pypredict QTH, example inside qth(LAT,LON,ALT)
* elNOAA - minimum elevation of NOAA satellites
* elMETEOR - minimum elevation of Meteor M2 satellite
* tleFileName - name and path of TLE file

###tledraw.py
Script for drawing satellite polar passes in PNG file:
* qth() - as in pypredict QTH, example inside qth(LAT,LON,ALT)
* elNOAA - minimum elevation of NOAA satellites
* elMETEOR - minimum elevation of Meteor satellite (Annex 1, 4.9dB when the satellite is 13deg above the horizon and 8.6 dB at 30deg or higher)
* tleFileName - name and path of TLE file
* passImgDir - directory name to put PNG files

###meteor_qpsk.py
Record 72k baseband, create INI files for Oleg's LRPT Offline Decoder. Adapted from otti's LRPT Airspy decoder
* bitstream_dir - where bitstream files will reside.
* lrpt_dir - Linux directory where ini files should be created
* rgb_lrpt_file - name of the RGB ini file
* mono_lrpt_file - name of the mono ini file (infrared)
* BITSTREAM_WINDOWS_DIR - wine/windows directory of bitstream (e.g. c:\\ - remember to put TWO backslashes)
* IMAGES_WINDOWS_DIR - wine/windows directory of created images (e.g. c:\\meteor\\ - same as above)

###update-keps.sh
This is a short shell script to update the keps, which are orbital
parameters needed by the predict program.  It is mostly copied from the PREDICT man
page. 
* TLEDIR - TLE files directory
