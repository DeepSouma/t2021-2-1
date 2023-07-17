def count_multiples(numbers, num_set):
    count_dict = {num: 0 for num in num_set}

    for value in numbers:
        for num in num_set:
            if value % num == 0:
                count_dict[num] += 1

    return count_dict
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = count_multiples(numbers, num_set)
print(result)

