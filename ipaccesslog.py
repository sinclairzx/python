#!/usr/bin/python -tt

import os
import sys
import re

def search(ip):
  o = open('access_log','rU')
  f = o.read()
 
  s = re.search(ip,f)
  if s:
    print s.group()
  else:
    print 'No match!'


def main():
  search([sys.argv[0]])

if __name__ == '__main__':
  main()



