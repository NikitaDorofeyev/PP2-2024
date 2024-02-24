import re

matches = []
pattern = r'\b[a-z]+_[a-z]+\b'

while True:
    text = input()
    if text == "":
        break

    current_matches = re.findall(pattern, text)
    matches.extend(current_matches)

print(matches)