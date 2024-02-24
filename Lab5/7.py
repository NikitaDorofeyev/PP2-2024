import re

def snake_camel(match):
    return match.group(1).upper()

with open("row.txt", "r", encoding="utf8") as file:
    text = file.read()

pattern = re.compile(r'_(\w)')

text_rows = pattern.sub(snake_camel, text)

print(text_rows)
