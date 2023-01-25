#creare un file di mille righe con il numero della riga generato da una stringa causale
import random
import string
filemio = open("filediprova.txt","w")
for i in range (100):
    print(i,random.choices(string.ascii_lowercase)) #il mio metodo
    filemio.write(str(i)+" "+"".join((random.choices(string.ascii_lowercase, k=100)))+"\n")
