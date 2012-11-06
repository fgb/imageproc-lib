#!/usr/bin/env python

"""
Write version and date information to a .c file, so compiles can be updated

authors: ronf, fgb, apullin
"""

import sys, os, time

VER_STR_LENGTH_MAX = 80

# Check and parse arguments
if len(sys.argv) < 2:
    print("Not enough arguments given. Need version string within single quotes.")
    sys.exit()

filename   = 'source/version-string.h'
fileheader = 'version.h'
version    = sys.argv[1] # version string within single quotes
date       = time.strftime("%a %b %d %H:%M:%S %Y")

fullstr = version + ': ' + date
verstr = fullstr[0:VER_STR_LENGTH_MAX] #limit version string length

# Write version and date information
fileout = open(filename,'w')
fileout.write(
'/* automatically generated by version.py - do not edit! */\n\n'      + \
'#define VERSION_STRING "'+ verstr + '"\n\n'      )
fileout.close()

print('updated ' + os.getcwd() + os.sep + filename)
