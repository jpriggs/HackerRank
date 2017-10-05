################################################################################################## 
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#
# A single string containing a time in 12-hour clock format (i.e. hh:mm:ssAM or hh:mm:ssPM), where
# 01 ≤ hh ≤ 12 and 00 ≤ mm, ss ≤ 59. Convert and print the given time in -hour format, where
# 00 ≤ hh ≤ 23.
#
# Coded by: Jason Rigdon
##################################################################################################


#!/bin/python3

import sys

from time import strptime, strftime
print(strftime("%H:%M:%S", strptime(input(), "%I:%M:%S%p")))
