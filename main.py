import datetime

a_date_time = datetime.datetime.now()
a_time = a_date_time.time()
print(a_time)

date = datetime.datetime.today()
print(date.strftime('%Y'))
print(date.strftime('%m'))
print(date.strftime('%d'))
print(date.strftime('%A'))



