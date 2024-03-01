import os

path_to_file = './Alphabet/'

os.mkdir(path_to_file)

for i in range (1, 27):
    letter = chr(i + 64)
    file = open(f'{path_to_file}{letter}', 'w')
    file.write(f"This is the letter {letter}, I was created from 6.py")