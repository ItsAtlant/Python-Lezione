# Esercizio 1:
# Usando Python: 
# •Scrivere su un file 'proverbio.txt' un proverbio a scelta
# •Aprire il file proverbio.txt
# •Leggerne tutto il contenuto
# •Scrivere i caratteri in posizione pari su un file 'file_proverbio_dispari.txt ' 
# •Scrivere i caratteri in posizione dispari su un file ‘file_proverbio_dispari.txt’ 
# Suggerimento: questa volta leggeteTUTTO il file e poi...

with open("proverbio.txt","w") as f:
    f.write("A buon cavallo non manca sella")

f = open("proverbio.txt","r")
lettura = f.read()
print(lettura)
lung = len(lettura)
provPari = open("provPari.txt","w")
provDispari = open("provDispari.txt","w")
for i in range (lung):
    if i%2 == 0:
        provPari.write(lettura[i])
    else:
        provDispari.write(lettura[i])
provPari.close()
provDispari.close()