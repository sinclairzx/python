#!/usr/bin/python -tt

def fix_start(s):
  first = s[0]
  rest = s[1:]
  full = rest.replace(first,'*')
  print first+full
  return

fix_start('ababbabababaaabbabdb')


