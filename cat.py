#!/usr/bin/python -tt

import sys

def cat(filename):
  f = open(filename,'rU')
  #for line in f:
  line = f.readlines()
  print line,
  f.close()

def main():
  cat(sys.argv[1])


if __name__ == '__main__':
  main()

