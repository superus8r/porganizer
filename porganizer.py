#!/usr/bin/env python

import sys
import datetime

today = datetime.date.today()
parsedDate = today.strftime('%d.%m.%Y')
extension = ".md"

message = "Please enter the file suffix: "
defaultFileName = "DailyLog"

# get the file suffix which comes after date in its name
# depending on the python version.
if sys.version_info[0] < 3:
    fileSuffix = raw_input(message) or defaultFileName
else:
    fileSuffix = input(message) or defaultFileName

fileName = parsedDate + '_' + fileSuffix + extension

print("Creating File: " + fileName)
file = open(fileName, "w+")
print("Done!")
