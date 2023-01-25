Alunni = ["Luca","Antonio","Gianna","Andrea","Barbara","Fabio","Giorgia","Michela","Lucia","Angela"]
Eta = [18,24,60,29,18,60,24,60,18,24]
dizionario = {}
while True:
    print("Per uscire digitare ESCI")
    x = input("Inserisci il nome ")
    if x == "ESCI":
        break
    Alunni.append(x)
    x = input("Inserisci l'eta ")
    Eta.append(x)


c = 0
lista = []
lung = len(Eta)
for x in range (lung):
    i = 1
    for i in range (lung):
        stringa = Alunni[x]
        if Eta[x] == Eta[i]:
            stringa += Alunni[i]
        if i == (range(lung-1)):
            dizionario[Eta[x]] = stringa
        
print(dizionario)
