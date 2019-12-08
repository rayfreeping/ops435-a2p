#!/usr/bin/env python3
# program name: checkA2p.py
# Copyrighted: Raymond Chan 2019

import sys

try:
    from a2_class import *
    print('Successfully import a2_class file.')
except:
    print('Error trying to import a2_class.')
    sys.exit(1)

try:
    print('Retriving Date class attributes: ...')
    date_attributes = dir(Date)
except:
    print('Retriving Date class attributes failed.')
    sys.exit(2)

print('Date class attributes:',date_attributes)
print('There are',len(date_attributes),'attributes')
expected_attributes = ['__init__',
                       '__str__',
                       '__repr__',
                       '__add__',
                       '__sub__',
                       'tomorrow',
                       'yesterday',
                       'day_of_week']

for attr in expected_attributes:
    if attr in date_attributes:
        print('Expected attributes <'+attr+'> found in Date Object.')
    else:
        print('Expected attributes <'+attr+'> missing in Date Object.')

try:
   print('Creating new date object named d1...')
   d1 = Date(2019,2,28)
   print('Creating new date object d1 successfully ->',d1)
except:
   print('Creating new data object failed.')
   sys.exit(3)

try:
   print('Checking __str__ method ...')
   str_date = str(d1)
except:
   print('Error calling __str__ method.')
   sys.exit(4)

if str_date != '2019/02/28':
    print('Incorrect or missing code --> ',str_date)
    print('Expected --> 2019/02/28')
else:
    print('Checking __str__ method: passed successfully.')

try:
   print('Checking __repr__ method ...')
   repr_date = repr(d1)
except:
   print('Error calling __repr__ method.')
   sys.exit(4)

if repr_date != '2019-02-28':
    print('Incorrect or missing code --> ',repr_date)
    print('Expected --> 2019-02-28')
else:
    print('Checking __repr__ method: passed successfully.')

try:
   print('Checking tomorrow method ...')
   tomorrow_date = d1.tomorrow()
except:
   print('Error calling tomorrow method.')
   tomorrow_date = 'Does not compute.'
#   sys.exit(5)

if str(tomorrow_date) != '2019/03/01':
   print('Incorrect result from tomorrow method -->',str(tomorrow_date))
   print('Expected --> 2019/03/01')
else:
   print('Checking tomorrow method: passed successfully.')

try:
   print('Checking yesterday method ...')
   yesterday_date = d1.yesterday()
except:
   print('Error calling yesterday method.')
   yesterday_date = 'Does not compute.'
#   sys.exit(6)

if str(yesterday_date) != '2019/02/27':
   print('Incorrect result from yesterday method -->',str(yesterday_date))
   print('Expected --> 2019/02/27')
else:
   print('Checking yesterday method: passed successfully.')

try:
   print('Checking day_of_week method ...')
   dow_date = d1.day_of_week()
except:
   print('Error calling day_of_week method.')
   dow_date = '-1'
#   sys.exit(7)

if dow_date != 4:
    print('Incorrect result from day_of_week method -->',dow_date)
    print('Expected --> 4')
else:
    print('Checking day_of_week method: passed successfully.')
