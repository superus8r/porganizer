#!/usr/bin/env python

import datetime

today = datetime.date.today()
parsedDate = today.strftime('%d.%m.%Y')

# get the file suffix which comes after date in its name
fileSuffix = raw_input("Please enter the file suffix: ") or "DailyLog"
fileName = parsedDate + '_' + fileSuffix

print("Creating File: " + fileName)
file = open(fileName, "w+")
print("Done!")