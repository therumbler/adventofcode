"""https://adventofcode.com/2020/day/1"""
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


def _find_mulitple_of_2020(numbers):
	go = True
	while go:
		try:
			number1 = numbers.pop()
			remaining = copy.deepcopy(numbers)
			print(len(remaining))
			while go:
				number2 = remaining.pop()
				sum = number1 + number2
				if sum == 2020:
					print('Found it!', number1, number2)
					return number1, number2
				if len(remaining) == 0:
					break
		except IndexError:
			print('end of list')
			return 

def day_one():
	print('hi')
	
	numbers = _load_numbers()
	# print(numbers)
	number1, number2 = _find_mulitple_of_2020(numbers)
	print('multiple', number1 * number2)
def main():
	day_one()


if __name__ == '__main__':
	main()