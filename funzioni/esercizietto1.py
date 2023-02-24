#create a function that get in inpyt a list of int numbers and get the summ of all the numbers
print("premere due volte spazio per uscire")
lista = []
def somma():
        sommanumeri = sum(lista)
        print(sommanumeri)
while True:
    numeri = input("Inserire i numeri: ")
    if numeri == "  ":
        break
    lista.append(int(numeri))
    
somma()

