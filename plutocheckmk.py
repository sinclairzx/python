#!/usr/bin/python -tt

import os
import re

def pluto_read():
  o = open('plutosn','rU')
  f = o.read()
  s = re.findall(r'(\w+\.\w+\.\w+\.\w+)\s\S+\s\w+\s\S\s\w+\s\w+\s\w+\s\S\s(\S+)',f)
 
#Basic print 
#  for ip,hostname in s:
#    print '\'' + hostname +'|titan|windows|supermicro\''

  for ip, hostname in s:
    if 'ESX' in hostname:
      print '\'' + hostname +'|titan|esx|supermicro\''
    elif 'MAIL' in hostname:
      print '\'' + hostname +'|titan|mail|supermicro\''
    elif 'SWITCH' in hostname:
      print '\'' + hostname +'|titan|switch\''
    elif 'ZEUS' in hostname:
      print '\'' + hostname +'|titan|zeus|supermicro\''
    elif 'DB' in hostname:
      print '\'' + hostname +'|titan|mysql\''
    else:
      print '\'' + hostname +'|titan\''
  return 
  o.close()


def main():
  pluto_read()


if __name__ == '__main__':
  main()
  
