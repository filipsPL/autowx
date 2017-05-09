#!/bin/bash
TLEDIR=/home/filips/github/autowx/tle/

rm $TLEDIR/weather.txt
wget --no-check-certificate -r http://www.celestrak.com/NORAD/elements/weather.txt -O $TLEDIR/weather.txt

rm $TLEDIR/noaa.txt
wget -r http://www.celestrak.com/NORAD/elements/noaa.txt -O $TLEDIR/noaa.txt

rm $TLEDIR/amateur.txt
wget -r http://www.celestrak.com/NORAD/elements/amateur.txt -O $TLEDIR/amateur.txt

rm $TLEDIR/cubesat.txt
wget -r http://www.celestrak.com/NORAD/elements/cubesat.txt -O $TLEDIR/cubesat.txt


rm $TLEDIR/multi.txt
wget -r http://www.pe0sat.vgnet.nl/kepler/mykepler.txt -O $TLEDIR/multi.txt

echo `date`
echo Updated