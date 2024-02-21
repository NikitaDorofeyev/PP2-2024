# Program to drop microseconds from datetime

import datetime

today = datetime.datetime.now()

today = today.replace(microsecond=0)

print(today)