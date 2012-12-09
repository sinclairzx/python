#!/usr/bin/python -tt

import os
import re

def pluto_read():
  o = open('plutosn','rU')
  f = o.read()
  s = re.findall(r'(\w+\.\w+\.\w+\.\w+)\s\S+\s\w+\s\S\s\w+\s\w+\s\w+\s\S\s(\w+)',f)
  if s:
    #print s.group(),
    print s
  else:
    print 'Match not found'


  o.close()

def main():
  pluto_read()


if __name__ == '__main__':
  main()
  
