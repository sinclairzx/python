#!/usr/bin/python -tt

import smtplib
import string

def sendemail():
  SUBJECT = 'This is a test python email'
  TO = 'andrew@sinweb.co.uk'
  FROM = 'elf@sinweb.co.uk'
  text = 'foo test email'
  BODY = string.join((
    'From: %s' % FROM,
    'To: %s' % TO,
    'Subject: %s' % SUBJECT,
    '',
    text
    ), '\r\n')
  server = smtplib.SMTP('localhost')
  server.sendmail(FROM, [TO], BODY)
  server.quit()

if __name__ == '__main__':
  sendemail()
