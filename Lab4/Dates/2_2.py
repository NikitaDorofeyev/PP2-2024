# Program to printy yesterday, today, tomorrow

import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"Yesterday was: {yesterday.strftime('%A, %B %d, %Y')}")
print(f"Today is: {today.strftime('%A, %B %d, %Y')}")
print(f"Tomorrow will be: {tomorrow.strftime('%A, %B %d, %Y')}")
