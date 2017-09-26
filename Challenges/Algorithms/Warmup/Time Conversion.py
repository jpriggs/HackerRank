#!/bin/python3

import sys

from time import strptime, strftime
print(strftime("%H:%M:%S", strptime(input(), "%I:%M:%S%p")))
