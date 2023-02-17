#scrivere una funzione che penda una lista di numeri come input e 
#restrituisca una lista contente solo i numeri pari. Utilizza
#unepressione lambda per definire la condizione di filtro 
#Esempio di imput [1,2,3,4,5]

numeri = [1,2,4,5,6,5,8]
numeriPari = list(filter(lambda x: x %2 == 0, numeri))
print(numeriPari)