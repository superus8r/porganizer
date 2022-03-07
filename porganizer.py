#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys
import os
import datetime
import re

extension = '.md'
defaultSuffix = 'DailyLog'
dateFormat = '%d.%m.%Y'
dateFormatRegex = '^..\\...\\.....'
separator = '_'
# Edit the following to tell how the left ToDo
# start in the previous file to copy the lines after it.
todoId = '--------'
# Edit the following to add before
# yesterday's ToDo if exists.
extraFreeSpace = '\n\n\n\n'

# keep track of last created log file if exists in the folder
# iterate the files in current folder and use the defined 
# date regex and file suffix to extract the dates only from 
# the log files.
# compare the dates to find the newest file

lastFileInFolder = ''
lst = os.listdir()
if (len(lst) > 0):
    tempDate = ''
    tempFileName = ''
    for fileName in lst:
        str = re.findall('(' + dateFormatRegex + ')' + separator + defaultSuffix, fileName)
        if len(str) < 1: continue
        fileDate = datetime.datetime.strptime(str[0], dateFormat)
        # if tempDate is empty, store this fileDate in it for comparision
        if not tempDate:
            tempDate = fileDate
            tempFileName = fileName
            continue
        # if the fileDate is newer than tempDate, 
        # replace tempDate with it
        if tempDate < fileDate:
            tempDate = fileDate
            tempFileName = fileName
    lastFileInFolder = tempFileName


# Create a new todo file for today if does not exist.

today = datetime.date.today()
parsedDate = today.strftime(dateFormat)
fileName = parsedDate + separator + defaultSuffix + extension

message = 'ℹ️  ' + fileName + ' will be created, continue?'
input(message)
    
# avoid creating the file if exists
if os.path.isfile(fileName):
    print('ℹ️  ' + fileName + ' already exists')
    print('💥 Abort!')
    sys.exit()

# create the file
print('🔄 Creating File: ' + fileName)
file = open(fileName, 'w+')
print('✅ File created!')

# open content of the last created log file in folder (if exists)
# if exists and copy the todo part to the new file
# if not, exit the program

yesterdayFile = None
try:
    yesterdayFile = open(lastFileInFolder, 'r')
except IOError:
    print('ℹ️  Yesterday\'s log file does not exist')
    file.close()
    sys.exit()


# The loop iterates through yesterday logs and looks for a todoId
# if the todoId is found, it sets the keepLine flag to True and
# it keeps the lines after todoId in todoLines list.

print('🔄 Copying ToDo from file: ' + lastFileInFolder)
keepLine = False
for line in yesterdayFile:
    words = line.split()
    if keepLine == False and len(words)>0 and words[0] == todoId:
        keepLine = True
        file.write(extraFreeSpace)
    if keepLine:
        file.write(line)
print('✅ Copied ToDo items from ' + lastFileInFolder)

# close both files
yesterdayFile.close()
file.close()

print('🚀 Have an amazing day!')


