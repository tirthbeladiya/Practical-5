fh = open('Practical-5.txt','w')
year = 2004
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            fh.write('It is a leap year.')
        else:
            fh.write('It is not a leap year.')
    else:
        fh.write('It is a leap year.')
else:
    fh.write('It is Not Leap Year.')
fh.close()
