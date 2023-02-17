numeri = [1,2,45,23,12,231,4,141,51,515,6,11]

def condizione(numeri):
    return numeri % 2 == 0

numeri_pari = list(filter(condizione, numeri))
print(numeri_pari)