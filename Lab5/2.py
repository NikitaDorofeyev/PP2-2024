import re

with open("row.txt", "r", encoding="utf8") as file:
    text = file.read()

matches = re.findall("[ab*]{2,3}", text)

print(matches)