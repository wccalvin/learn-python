#!/usr/bin/env python

my_emailText = 'From clayton.calvin@gmail.com Tue Mar 6'

# Get only the domain names

startIndex = my_emailText.find('@')
endIndex = my_emailText.find(' ', startIndex)  # read find documentation
emailDomain = my_emailText[startIndex+1:endIndex]

print('Email Domain: {}'.format(emailDomain))