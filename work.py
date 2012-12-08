#!/usr/bin/python -tt
import sys

def hello(name):
  newname = name.lower()
  if newname == 'alice':
    print 'Oh Oh! Wrong system!'
  else:
    print 'Hello', newname

	
hello(sys.argv[1])
