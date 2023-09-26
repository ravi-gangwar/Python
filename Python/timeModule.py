import time 
a = int(time.strftime('%H'))

if (a>=0 and a<12):
    print('Hello harry bhai "GOOD MORNIG"')
elif (a>=12 and a<18):
    print('Hello harry bhai "GOOD AFTERNOON"')
else:
    print('Hello harry bhai "GOOD EVENING"')