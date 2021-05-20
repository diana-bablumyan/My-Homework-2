import os
import random

path = os.getcwd()
new_path = os.path.join(path, 'My_file.txt')

for i in range(21):
	x  = random.randint(1, 100)
	if x % 2 != 0:
		x = str(x)
		with open(new_path, 'a') as file:
			file.write(x)
			file.write('\n')

sum_numbers = 0 

with open(new_path, 'r') as file:
	for i in range(63):
		try:
			sum_numbers += int(file.readline())
		except ValueError:
			continue

	print(sum_numbers)
		