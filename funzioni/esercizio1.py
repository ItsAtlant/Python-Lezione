#if the user write and the leght of the text is even write it in a file even if its odd write it in a file odd

#No output, need a debug
print("Per uscire premi due volte invio")

while True:
    nome = input("Inserire il testo: ")
    if nome == "  ":
        break
    lenght = len(nome)
    def primafunzione():
        def parifunzione():
                f = open("even.txt","w")
                f.write(nome)
                print("pari")
        def disparifunzione():
                f = open("odd.txt","w")
                f.write(nome)
                print("dispari")
        if lenght%2 == 0:
            parifunzione()
        else:
            disparifunzione()
    primafunzione()
