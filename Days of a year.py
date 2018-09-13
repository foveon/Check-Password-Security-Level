year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
 
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print ('data error')
sum += day
leap = 0

if ((year%4==0)and(year%100!=0)) or((year%100==0)and(year%400==0)):
    Dth=months[month-1]+day
else:
    Dth=months[month-1]+day
print ("it is the %dth day "%Dth+"of year "+str(year))
