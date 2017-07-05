#!/bin/bash
source /home/mtib/env.sh
ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 -y \
	$SURV/$SPIC/$(date +%Y_%m_%d_%H_%M).jpg > /dev/null 2>&1;
