def sum_negative_numbers(numbers):
    count_negative_numbers = 0
    for number in numbers:
        if number < 0:
            count_negative_numbers += 1
    return count_negative_numbers

print(sum_negative_numbers([1, 2, -1, -2, -3, 4, -6]))