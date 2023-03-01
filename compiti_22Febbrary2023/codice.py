# TODO:Far mettere il path del salvataggio del report 
# TODO:Scrivere una funziona da riga 19 a 24 e importarla esternamente
# TODO:Salvare il report in un altro file
import requests

link = input("Inserisci il link: ")
site = requests.get(link) 

path = input("Iserisci il path per salvare il SITO: ") 
Reportpath = input("Inserisci il path per salvare il REPORT: ")

with open(path,'w') as f:

    f.write(site.text)

i,k,c = 0,0,0

with open (path,"r") as f, open(Reportpath,"w") as f2:
    file = f.read()
    for x in range (len(file)):
        if "img " == file[x:x+4]:
            i = i + 1
        if "class=" == file[x:x+6]:
            k = k + 1
        if "href" == file[x:x+4]:
            c = c + 1
    f2.write("Nel file ci sono:\n")
    f2.write(f"{i} immagini\n")
    f2.write(f"{k} classi\n")
    f2.write(f"{c} siti\n")
print("Nel file ci sono:")
print(i,"immagini",k,"classi",c,"link") 