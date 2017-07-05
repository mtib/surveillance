#!/bin/bash
source /home/mtib/env.sh
rm $SURV/$SVID/*.mp4 || :;
for i in 10 24 30 60; do
	ffmpeg  -framerate $i \
		-pattern_type glob \
		-i "$SURV/$SPIC/*.jpg" \
		-c:v libx264 -y \
		$SURV/$SVID/${LPRE}_${i}_${LSUF} > /dev/null 2>&1;
done
