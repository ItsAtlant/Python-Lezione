my_comp = [x ** 2 for x in range (10000) if x % 2 == 0]

print(my_comp)

def prova_generatpre ():
    prova_generatpre.count += 1
    yield "Hello"
    prova_generatpre.count += 1
    yield "word"
    prova_generatpre.count += 1
    yield "osss"

prova_generatpre.count = 0 
for i in prova_generatpre():
    print(i)
print(prova_generatpre.count)