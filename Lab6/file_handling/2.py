import os

specified_path = input('Please, Enter the path to check: ')

existence = os.access(specified_path, os.F_OK)
readability = os.access(specified_path, os.R_OK)
writability = os.access(specified_path, os.W_OK)
executability = os.access(specified_path, os.X_OK)

print(f'Exists?: {existence}')
print(f'Readable?: {readability}')
print(f'Writable?: {writability}')
print(f'Executable?: {executability}')