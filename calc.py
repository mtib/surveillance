#!/bin/env python3
import math

# delay in minutes
# size in kb
# storage in Gb
def days(delay, size=38, storage=8):
    return (storage*1024**2 / size) / (60/delay * 24)

# delay in minutes
# framerate in hz
# duration in years
def scale(delay, framerate, duration=1):
    delay = float(delay)
    framerate = float(framerate)
    duration = float(duration)

    print("INPUT:  [{}m, {}Hz, {}y]".format(delay, framerate, duration))
    print("{:7.2f} minutes between pictures".format(delay))
    print("{:7.2f} Hz output framerate".format(framerate))
    print("\nOUTPUT: [intermediate]")
    pih = 60 / delay
    print("{:7.2f} pictures in an hour".format(pih))
    his = framerate / pih
    print("{:7.2f} hours in a second".format(his))
    dis = his / 24
    print("{:7.2f} days in a second".format(dis))
    print("{:7.2f} seconds per day".format(1/dis))
    dur = (365 * duration) / dis
    print("\nOUTPUT: [final]")
    print("{:7.0f} seconds in {:.1f} year(s)".format(dur, duration))
    print("{:4.0f}:{:02.0f} minutes in {:.1f} year(s)".format(math.floor(dur/60), (dur%60), duration))
    print("{:7.0f} times scale".format(delay*framerate*60))

if __name__ == "__main__":
    import sys
    a = sys.argv[1:];
    if len(a) != 0:
        if len(a) == 1:
            scale(a[0], 60)
        elif len(a) == 2:
            scale(a[0], a[1])
        else:
            scale(a[0], a[1], a[2])
    else:
        scale(15,60)

