#!/bin/env python3
import os
import sys
import subprocess
import math

def getFilesWith(folder, suffix):
    files = [os.path.join(folder,img) for img in os.listdir(folder) if img[-len(suffix):] == suffix]
    files.sort()
    return files

def compare(p1, p2, diff="/tmp/py_diff.png"):
    cmd = ["compare", "-metric", "PSNR", p1, p2, diff]
    pipe = subprocess.run(cmd, stderr=subprocess.PIPE, encoding="utf-8")
    return float(pipe.stderr)

def compareLast(folder):
    images = getFilesWith(folder, ".jpg")
    diff = compare(images[-2], images[-1])
    return diff

def compareAll(folder):
    images = getFilesWith(folder, ".jpg")
    extremsig = [2**32, 0]
    extremimg = [["empty", "empty"],["empty", "empty"]]
    sep = 2
    for i in range(len(images)-sep):
        current = [images[i], images[i+sep]]
        signal = compare(*current)
        if signal < extremsig[0]:
            extremsig[0] = signal
            extremimg[0] = current[:]
        if signal > extremsig[1]:
            extremsig[1] = signal
            extremimg[1] = current[:]
        print("{:3d}%".format(math.ceil(float(i)/(len(images)-sep)*100)), images[i], "to", images[i+sep], "->", signal)
    return (extremsig, extremimg)

def compareDeleteThree(folder, delThresh=30.0, limitTo=300):
    images = getFilesWith(folder, ".jpg")[-limitTo:]
    compare1 = []
    compare2 = []

    n = len(images)-1
    m = len(images)-2
    Z = (n + m)*1.0
    for i in range(n):
        compare1.append(compare(images[i], images[i+1]))
        print("{:3d}% {} vs {} -> {}".format(math.floor((i+1.0)/Z*100), images[i], images[i+1], compare1[i]))
    for i in range(m):
        compare2.append(compare(images[i], images[i+2]))
        print("{:3d}% {} vs {} -> {}".format(math.floor((i+n+1.0)/Z*100), images[i], images[i+2], compare2[i]))

    todelete = []
    print("selected:")
    for i in range(len(images)-2):
        m = min(compare1[i], compare2[i], compare1[i+1])
        if m > delThresh:
            print(" - {} ({})".format(images[i+1], m))
            todelete.append(images[i+1])
    if len(todelete) == 0:
        print("nothing")
    return todelete

if __name__ == '__main__':
    i = 1
    arg = sys.argv[:]
    while i < len(arg):
        if arg[i] == "-folder":
            i = i + 1
            diff = compareLast(sys.argv[i])
            print(diff)
        elif arg[i] == "-all":
            i = i + 1
            diff, images = compareAll(sys.argv[i])
            def _fmt(signal, imgs, index, name):
                return "{}: {} to {} with {}".format(name, imgs[index][0], imgs[index][1], signal[index])
            print(_fmt(diff, images, 0, "minimum"))
            print(_fmt(diff, images, 1, "maximum"))
        elif arg[i] == "-delete":
            i = i + 1
            dels = compareDeleteThree(arg[i])
            for img in dels:
                os.remove(img)
        elif arg[i] == "-clean":
            i = i + 2
            moves = compareDeleteThree(arg[i-1])
            for img in moves:
                os.rename(img, os.path.join(arg[i], os.path.basename(img)))
        elif arg[i] == "-compare":
            diff = compare(arg[i+1], arg[i+2])
            i = i + 2
            print(diff)
        else:
            print("unknown subcommand:", arg[i])
        i = i + 1
    
