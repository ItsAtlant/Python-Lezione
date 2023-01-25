# Creare un file con un testo a scelta suddiviso in righe e colonne (vedi ad esempio: https://it.lipsum.com/) 
# •Il file potrebbe essere potenzialmente enorme
# •Fino a che l'utente non scrive la singola lettera 'q’
# •Leggere Una Parola Da Input
# •Se la parola è presente nel file indicare la riga e la Colonna
# •Altrimentiscrivere'Parolanonpresente’


#qui prendo il mio file originale e lo ricopio senza punti e virgole su un altro file 
remove = ",.;:'()?!"   #i caratteri che voglio togliere
with open("filesenzapuntievirgole.txt","w") as f2,open("loremIpsum.txt","r") as f :
    file = f.read()
    for x in range (len(remove)):
        file = file.replace(remove[x],"")
    f2.write(file)
with open("filesenzapuntievirgole.txt","r") as f2:
    riga = f2.readlines()
    while True:
        parola = input("inserire la parola: ")
        word = False
        if parola == "q":
            break
        for k in range (len(riga)):
            riga2 = str(riga[k])
            colonna = riga2.split()
            for i in range (len(colonna)):
                if colonna[i] == parola:
                    print("parola trovata in colonna",i+1," e in riga",k+1)
                    word = True
        if word == False:
            print("non c`e la parola")

