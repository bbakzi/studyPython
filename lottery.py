from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    winning_nums = generate_numbers(7)
    return sorted(winning_nums[:6]) + winning_nums[6:]


print(draw_winning_numbers())


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    num_match = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_match = count_matching_numbers(numbers, winning_numbers[6:])

    if num_match == 6:
        return 100000000
    elif num_match == 5 and bonus_match == 1:
        return 50000000
    elif num_match == 5:
        return 1000000
    elif num_match == 4:
        return 50000
    elif num_match == 3:
        return 5000
    else:
        return 0

