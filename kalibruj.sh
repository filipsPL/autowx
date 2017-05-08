#!/bin/bash

#kal -s GSM900 -e 61
kal -c 25 -g 49.6 -e 61 2> /dev/null | tail -1 | cut -d " " -f 4
