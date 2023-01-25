import random
import string
filemio = open("filediprova.txt","w")
filescritturaPARI = open("filepari.txt","w")
filescritturaDISPARI = open("filedispari.txt","w")
for i in range (100):
    filemio.write(str(i)+" "+"".join((random.choices(string.ascii_lowercase, k=100)))+"\n")

filemio.close()

filemio = open("filediprova.txt","r")
for i in range(100):
    l = filemio.readline()
    if i %2 == 0 :
        filescritturaPARI.write(l)
    else:
        filescritturaDISPARI.write(l)

x = enumerate(filemio)
print (x)
filemio.close()
filescritturaPARI.close()
filescritturaDISPARI.close()
    