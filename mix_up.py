#!/usr/bin/python -tt

def mix_up(a, b):
  aa = a[:2]
  bb = b[:2]
  aarest = a[2:]
  bbrest = b[2:]
  print bb+aarest, aa+bbrest
  return

mix_up('mix','pod')

