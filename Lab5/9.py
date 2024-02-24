import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

s = input()
result = insert_spaces(s)
print(result)
