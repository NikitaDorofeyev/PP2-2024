def toZero(n):
    while n >= 0:
        yield n
        n -= 1

number = int(input("To zero from: "))

result = toZero(number)

for num in result:
    print(num)