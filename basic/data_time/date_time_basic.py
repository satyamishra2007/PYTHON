from datetime import datetime, date, timedelta

today_ts = datetime.today()
print(f'today_ts : {today_ts}')

now = datetime.now()
print(f'now : {now}')

today = date.today()
print(f'today :{today}')

print(now - timedelta(days=5))
print(now - timedelta(days=5, hours=5))

print(today - timedelta(days=3))


'''
Python strftime() - datetime object to string

The strftime() method is defined under classes date, datetime and time. 
The method creates a formatted string from a given date, datetime or time object.
'''
print(today.strftime('%m/%d/%y'))




'''
Python strptime() - string to datetime
The strptime() method creates a datetime object from a given string (representing date and time).

'''
date_string = "21 June, 2018"
print(datetime.strptime(date_string, "%d %B, %Y"))
