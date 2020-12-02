import copy

def _load_numbers():
	numbers = []
	with open("dayoneinput.txt") as f:
		while True:
			number = f.readline().strip()
			if not number:
				break

			numbers.append(int(number))
	return numbers


def _find_sum_of_2020(numbers):
	go = True
	while go:
		try:
			number1 = numbers.pop()
			remaining = copy.deepcopy(numbers)
			print(len(remaining))
			while go:
				number2 = remaining.pop()
				while go:
					number3 = remaining.pop()
					sum = number1 + number2 + number3
					if sum == 2020:
						print('Found it!', number1, number2, number3)
						return number1, number2, number3
					if len(remaining) == 0:
						print('non remaining')
						break
		except IndexError:
			print('end of list')
			return None, None, None



def _find_3_numbers_that_add_to_2020(numbers):
	for number1 in numbers:
		for number2 in numbers:
			for number3 in numbers:
				if number1 + number2 + number3 == 2020:
					return number1, number2, number3
	# three_numbers = [n1, n2, n3 for n1 in numbers for n2 in number for n3 in numbers if n1+n2+n3=2020]
	print(three_numbers)
	return None, None, None

def day_one_part_two():
	print('hi')
	
	numbers = _load_numbers()
	# print(numbers)
	number1, number2, number3 = _find_3_numbers_that_add_to_2020(numbers)
	if not number1:
		print('ERROR: none found')
	else:
		print('multiple', number1 * number2 * number3)

def main():
	day_one_part_two()


if __name__ == '__main__':
	main()