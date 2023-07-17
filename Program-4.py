def get_multiples_count(numbers):
    multiples_count = {}

    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] = multiples_count.get(i, 0) + 1

    return multiples_count
    
numbers=[]
n=int(input())
for i in range(n):
    a=int(input())
    numbers.append(a)
result=get_multiples_count(numbers)
print(result)