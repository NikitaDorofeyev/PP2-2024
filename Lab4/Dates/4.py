# Program to calculate two dates difference in seconds

from datetime import datetime

def date_difference_in_seconds(date1, date2):

    dt1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    diff_seconds = abs((dt2 - dt1).total_seconds())
    return diff_seconds

date1_input = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_input = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

difference = date_difference_in_seconds(date1_input, date2_input)
print("Difference in seconds:", difference)