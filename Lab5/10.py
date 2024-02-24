import re

def snake_camel(match):
    return '_' + match.group(1).lower()

text = input("Enter the text containing snake_case strings: ")

pattern = re.compile(r'([A-Z])')

text_rows = pattern.sub(snake_camel, text)

print(text_rows)
