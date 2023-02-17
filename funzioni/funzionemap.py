def somma(numeri1,numeri2):
    return numeri1+numeri2

for n in map(somma, [1,2,3],[4,5,6]):
    print(n)