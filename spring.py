#!/usr/bin/python -tt

def both_ends(s):
  ss = len(s)
  if ss > 2:
    dd = s[:2]
    print dd
    ee = s[-2:]
    print ee
    print dd+ee
    print s[:2]+s[-2:]
  else:
    print ''
  return

both_ends('Andrew')


