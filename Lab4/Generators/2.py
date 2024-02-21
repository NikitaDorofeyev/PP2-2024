# Program which print even numbers between 0 and n in comma separated form

def generate_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input("Even numbers between 0 and: "))

even_numbres = generate_even(n)

for even in even_numbres:
    print(even, end=", ")