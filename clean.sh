#!/bin/bash
source /home/mtib/env.sh
mkdir $SURV/Deleted > /dev/null 2>&1 || :;
$HOME/similar.py -clean $SURV/$SPIC $SURV/Deleted > /dev/null 2<&1
