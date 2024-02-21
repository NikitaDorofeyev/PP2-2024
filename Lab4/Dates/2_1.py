# Program to printy yesterday, today, tomorrow

import datetime

today = datetime.datetime.now().date()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"Yesterday was: {yesterday}\nToday is: {today}\nTomorrow will be: {tomorrow}")