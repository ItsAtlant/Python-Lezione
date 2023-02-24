def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

########

def generate_numbers(n):
    for i in range(n):
        yield i

my_iter = generate_numbers(10)
print(next(my_iter))