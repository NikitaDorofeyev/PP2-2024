import re

with open("row.txt", "r", encoding="utf8") as file:
    text = file.read()

pattern = re.compile(r'[ ,.]')
text_rows = pattern.sub(":", text)

print(text_rows)
