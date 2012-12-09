#!/usr/bin/python -tt

import os
import sys
import re

def search():
  o = open('access_log','rU')
  f = o.read()

#test read in file
#  print f

  match = re.search(r'\w+\.\w+\.\w+\.\w+',f)
  if match: 
    print match.group()
  else: 
    print 'Match not found!'

def main():
  search()


if __name__ == '__main__':
  main()

