#!/usr/bin/env python3

import csv
from pathlib import Path
from better_profanity import profanity
import re,json,sys

#get single nick from the line
def getNickFromLine(line):
    try:
        found = re.search('<(.+?)>', line).group(1)
    except AttributeError:
        found = '' # apply your error handling
    if found and found != '':
        return found
    else:
        return 'errorPleaseCheck'

# check if there is profanity in the string
def isProf( str ):
    if profanity.contains_profanity(str):
        nick = getNickFromLine(str)
        return {'nick':nick, 'string': str}
    else:
        return False

#get all nicks 
#this will only get nicks as first occurrences 
def getNicks(file):
    nicks={}
    with open(file) as fp:
        while True:
            line = fp.readline()
            nicks[getNickFromLine(line)] = 0
            if not line:
                break
    return nicks

# count lines spoken by nick 
def countNickLines(file,allNicks):
    with open(file) as fp:
        while True:
            line = fp.readline()
            allNicks[getNickFromLine(line)] += 1 
            if not line:
                break
    return allNicks

if len(sys.argv) <= 1:
    print("forgot to supply file")
    sys.exit()

# staaart
all_nicks = getNicks(sys.argv[1])
countnicks = countNickLines(sys.argv[1],getNicks(sys.argv[1]))

#main loop
with open(sys.argv[1]) as fp:
    while True:
        line = fp.readline()
        profRes= isProf(line)
        if profRes:
            all_nicks[profRes['nick']]+=1
        if not line:
            break 


print("nick,number of profane lines,number of total lines,percentage per total lines")
for i in all_nicks:
    percentage = all_nicks[i] / countnicks[i] * 100
    print(i,",",all_nicks[i],",",countnicks[i],",",percentage)
