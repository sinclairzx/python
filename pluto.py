#!/usr/bin/python -tt

import os
import re

def pluto_read():
  o = open('plutosn','rU')
  f = o.read()
  s = re.findall(r'(\w+\.\w+\.\w+\.\w+)\s\S+\s\w+\s\S\s\w+\s\w+\s\w+\s\S\s(\S+)',f)
  #if s:
    #print s.group(),
    #print s
  #else:
    #print 'Match not found'
  
  for ip,hostname in s:
    print ip, '   ', hostname
  return
  o.close()

def main():
  pluto_read()


if __name__ == '__main__':
  main()
  
