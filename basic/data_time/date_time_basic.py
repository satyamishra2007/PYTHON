from datetime import datetime,date,timedelta

today_ts = datetime.today()
print(today_ts)

now = datetime.now()
print(now)

today = date.today()
print(today)

print(now - timedelta(days= 5))
print(now - timedelta(days= 5,hours= 5))
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
print(datetime.strptime(date_string,"%d %B, %Y"))
