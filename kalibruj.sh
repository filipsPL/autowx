#!/bin/bash

recentShift=`cat var/dongleshift.txt`

#kal -s GSM900 -e 61
kal -c 116 -g 49.6 -e $recentShift 2> /dev/null | tail -1 | cut -d " " -f 4 | tee var/dongleshift.txt
