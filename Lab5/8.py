import re

def split_at_uppercase(match):
    pattern = r'[A-Z][^A-Z]*'
    return re.findall(pattern, match)

with open("row.txt", "r", encoding="utf8") as file:
    text = file.read()

result = split_at_uppercase(text)

print(result)
