word = input()

def count_letters(word):
    upper_count = 0
    lower_count = 0

    for letter in word:
        if letter.isupper():
            upper_count += 1
        else:
            lower_count += 1

    return upper_count, lower_count

result = count_letters(word)

upper, lower = result

print(f"The number of upper case letters is {upper}\nThe number of lower case letters is {lower}")

