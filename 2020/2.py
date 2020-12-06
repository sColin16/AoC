
with open('2-input.txt', 'r') as f:
    valid = 0
    for line in f:
        num_range, letter, password = line.split()

        min_num, max_num = num_range.split('-')
        min_num, max_num = int(min_num), int(max_num)
        letter = letter[0]

        letter_count = password.count(letter)

        if min_num <= letter_count <= max_num:
            valid += 1

print(valid)

with open('2-input.txt', 'r') as f:
    valid = 0

    for line in f:
        num_range, letter, password = line.split()

        min_num, max_num = num_range.split('-')
        min_num, max_num = int(min_num), int(max_num)
        letter = letter[0]

        if password[min_num - 1] == letter and password[max_num - 1] != letter:
            valid += 1

        elif password[min_num - 1] != letter and password[max_num - 1] == letter:
            valid += 1

print(valid)
