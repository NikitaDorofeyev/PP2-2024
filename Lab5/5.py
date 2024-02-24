import re

matches = []
pattern = r'a.*b'

while True:
    text = input()
    if text == "":
        break

    current_matches = re.findall(pattern, text)
    matches.extend(current_matches)

print(matches)
 