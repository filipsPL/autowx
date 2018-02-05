#!/bin/bash

OUTPUT_DIR="/home/dane/nasluch/sat/img/"`date +"%Y/%m/%d"`
mkdir -p $OUTPUT_DIR

recentShift=`cat var/dongleshift.txt`

rtl_power -f 118M:144M:8k -g 50 -i 10 -e 120m -p $recentShift $OUTPUT_DIR/scanner.csv
external/gopow.x64 -i $OUTPUT_DIR/scanner.csv -o $OUTPUT_DIR/scanner.png
bzip2 $OUTPUT_DIR/scanner.csv
