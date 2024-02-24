import re

with open("row.txt", "r", encoding="utf8") as file:
    text = file.read()

matches = re.findall(r'\b[A-Z]+[a-z]+\b', text)

print(matches)
