def reverse(result):
    words = result.split()

    for i in reversed(words):
        print(i, end= "")


user = input()

reverse(user)