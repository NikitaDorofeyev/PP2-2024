def palindrom(word):
    if word == word[::-1]:
        return True
    return False

word = input()

result = palindrom(word)

if(result):
    print("It is a Palindrom)")
else:
    print("It is not a Palindrom(")