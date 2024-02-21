# Program to subtract five days from current date

import datetime

today = datetime.datetime.now()

new_date = (today - datetime.timedelta(days=5)).date()

print(new_date)




