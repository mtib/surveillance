#!/bin/bash
source /home/mtib/env.sh
cd $SURV && python -m http.server 8122 > /dev/null 2>&1 &
