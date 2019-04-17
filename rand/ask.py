#!/usr/bin/python
import serial
import syslog
import time
import os
import json
import math
import string
import re

port = '/dev/tty.usbmodem1421'
ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

nums = []
readme = False

def myRandom(num):
    i = 0
    sessionNums = []
    while (i < 6):
        value = str(ard.readline())
        time.sleep(0.5)
        line = int(re.sub("\D", "", value))
        sessionNums.append(line)
        print("." * i)
        i += 1
    for number in sessionNums:
        currentNum = math.sqrt(num * number)
        currentNum = str(currentNum).split(".")
        currentNum = int(currentNum[0]) * int(currentNum[1])
        for d in [int(d) for d in str(int(currentNum))]:
            nums.append(d)
    num = currentNum
    return nums[-1]


def scale(minNum, maxNum, scaleMe):
    OldRange = (max(nums) - min(nums))
    if (OldRange == 0):
        randInt = minNum
    else:
        NewRange = (maxNum - minNum)  
        randInt = (((scaleMe - min(nums)) * NewRange) / OldRange) + minNum
    return randInt


def getQuery():
    num = 1

    with open("./poetry.json", "r") as f:
        poetry = json.load(f)

    print("Seeking an answer...")

    randInt = myRandom(num)
    num += randInt
    poetIndex = int(scale(0, (len(poetry) -1), randInt))
    poet = poetry[poetIndex]
    
    randInt2 = myRandom(num)
    num += randInt

    poemIndex = int(scale(0, (len(poet['poems']) -1), randInt2))
    poem = poet['poems'][poemIndex]

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(str(poetIndex) +","+ str(poemIndex))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1.5)

    print(poet['symbol'].upper())
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1.75)

    print(poem['title'])
    print("by " + poet['poet'])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1.75)

    for line in poem['text']:
        print(line)
        time.sleep(1.3)


input("For what do you need clarity? ")
getQuery()