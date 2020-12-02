


def _load_passwords():
	with open("daytwoinput.txt") as f:
		text = f.read()

	return text.split("\n")


def _is_valid_part_1(input):
	# print(password)
	range = input[0:input.find(" ")].split("-")
	range = [int(n) for n in range]
	# print(range)
	letter = input[input.find(" ") + 1:input.find(":")]
	password = input[input.find(":") + 1:].strip()
	# print(range, letter, password)

	count = password.count(letter)
	# print('count = ', count)
	if count < range[0]:
		return False
	if count > range[1]:
		return False
	return True


def _is_valid_part_two(input):
	range = input[0:input.find(" ")].split("-")
	range = [int(n) for n in range]
	# print(range)
	letter = input[input.find(" ") + 1:input.find(":")]
	password = input[input.find(":") + 1:].strip()

	first_match = password[range[0] -1] == letter
	second_match = password[range[1]-1] == letter
	is_valid = first_match ^ second_match
	# print(range, letter, password, first_match, second_match, is_valid)
	return is_valid

def main():
	passwords = _load_passwords()
	# print(passwords)

	valid_list = list(map(_is_valid_part_1, passwords))
	print("Answer Part 1:", len([v for v in valid_list if v]))
	


	# Part Two
	valid_list = list(map(_is_valid_part_two, passwords))
	print("Answer Part 2:", len([v for v in valid_list if v]))
if __name__ == '__main__':
	main()