#!/usr/bin/python -tt
import sys
import urllib
import re

def get_url():
  url = urllib.urlopen('http://www.sinweb.co.uk/remote.html')
  page = url.read()
  se = re.search('superman',page)
  if se:
    print se.group(), 'is alive, your webpage is up!'
  else:
    print 'Match not found, webpage is down!' 

get_url()
