def isPalindrom(word):
    if word == word[::-1]:
        return True
    return False

word = input()

if isPalindrom(word):
    print("Yes, a passed string is indeed a palindrome")
else:
    print("Sorry user, pallindrom wasn't part of our deal")