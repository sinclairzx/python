#!/usr/bin/python -tt

#import the modules we will need
import re
import os

#get the sysem type
sysinfo = os.uname()

#search for the system name (str) in the system info

if re.search('elf',str(sysinfo)):
  print 'This is the elf system'
else:
  print 'Oops! This is the wrong system!'


