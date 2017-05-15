##
## Config header, sorry
## TODO: Better config system
##
systemDir='/home/filips/github/autowx/'
# Satellite names in TLE plus their frequency
#satellites = ['NOAA 18','NOAA 15', 'NOAA 19', 'METEOR-M 2']
satellites = ['NOAA 18','NOAA 15', 'NOAA 19']
#freqs = [137912500, 137620000, 137100000, 137900000]
freqs = [137912500, 137620000, 137100000]
# Dongle gain
dongleGain='49.8'
#
# Dongle PPM shift, hopefully this will change to reflect different PPM on freq
dongleShift='63'
#
# Dongle index, is there any rtl_fm allowing passing serial of dongle? Unused right now
dongleIndex='0'
#
# Sample rate, width of recorded signal - should include few kHz for doppler shift
sample ='48000'
sampleMeteor='200000'
# Sample rate of the wav file. Shouldn't be changed
wavrate='11025'
#
stationLat='52.3404'
stationLon='-21.0579'
stationAlt='111'
tleDir=systemDir+'/var/tle/'
tleFile='weather.txt'
# Minimum elevation
minElev='20'
minElevMeteor='35'
decodeMeteor='no'
# Should I remove RAWs after transcoding?
removeRAW='yes'
# Directories used in this program
wxInstallDir='/usr/local/bin'
# Recording dir, used for RAW and WAV files
#
recdir='/home/dane/nasluch/sat/rec'
#
# Spectrogram directory, this would be optional in the future
#
specdir='/home/dane/nasluch/sat/spectro'
#
# Output image directory
#
imgdir='/home/dane/nasluch/sat/img'
#
# Map file directory
#
mapDir='/home/dane/nasluch/sat/maps'

# Options for wxtoimg
# Create map overlay?
wxAddOverlay='yes'
# Image outputs
# Create other enhancements?
wxEnhCreate='yes'
# List of wxtoimg enhancements, please read docs
# Commons are: MCIR, MSA, MSA-precip, HVC, HVC-precip, HVCT, HVCT-precip, therm
wxEnhList = [ 'MCIR-precip', 'HVC', 'MSA', 'therm' ]
# Turning it off creates empty logs...
wxQuietOutput='no'
# Decode all despite low signal?
wxDecodeAll='yes'
# JPEG quality
wxJPEGQuality='72'
# Adding overlay text
wxAddTextOverlay='yes'
wxOverlayText='SOME TEXT'
# Overlay offset - wxtoimg
# Negative value - push LEFT/UP
# Positive value - push RIGHT/DOWN
wxOverlayOffsetX='0'
wxOverlayOffsetY='0'
#
# Various options
# Should this script create spectrogram : yes/no
createSpectro='yes'
#
# SCP Config, works best with key authorization
#
SCP_USER=''
SCP_HOST=''
SCP_DIR=''
# Send LOG with imagefile?
LOG_SCP='n'
# Send image to remote server?
IMG_SCP='n'
# Logging
loggingEnable='y'
logFileName='/home/dane/nasluch/sat/logs/noaacapture.log'
scriptPID='/home/dane/nasluch/sat/logs/noaacapture.pid'
statusFile='/tmp/info_file'
# SFPG
sfpgLink='n'

# dongle shift file
dongleShiftFile=systemDir + "var/dongleshift.txt"
