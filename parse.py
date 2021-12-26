#!/usr/bin/env python3
from pathlib import Path
from better_profanity import profanity
import re,sys

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

if len(sys.argv) <= 1:
    print("forgot to supply file")
    sys.exit()

# start
all_nicks = getNicks(sys.argv[1])
count_nicks = getNicks(sys.argv[1])

#main loop

with open(sys.argv[1]) as fp:
    while True:
        line = fp.readline()
        count_nicks[getNickFromLine(line)]+=1
        profRes= isProf(line)
        if profRes:
            all_nicks[profRes['nick']]+=1
        if not line:
            break 
#Filter out nicks with less than 50 lines
filtered_count_nicks=dict(filter(lambda val: val[1] > 50 , count_nicks.items()))

print("nick,number of profane lines,number of total lines,percentage per total lines")
for i in filtered_count_nicks:
    percentage = all_nicks[i] / filtered_count_nicks[i] * 100
    print(i,",",all_nicks[i],",",filtered_count_nicks[i],",",percentage)
