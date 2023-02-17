quadrato = lambda x : x * x
y = (lambda x :x * x)(16)
print(y)

add_numbers = lambda x, y: x+y
print(add_numbers(3,4))

lista = [1,23,4,5,56,643,264,62,34,2346,432,6234,52,3,43252,364,3262,46,236,26,56,7,6,76,786]
filtered_list = list(map(lambda x: x**2,lista))
print(filtered_list)