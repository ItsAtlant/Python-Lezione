# TODO:Far mettere il path del salvataggio del report 
# TODO:Scrivere una funziona da riga 19 a 24 e importarla esternamente
# TODO:Salvare il report in un altro file
import requests

image_url = input("Inserisci il link: ")
  

site = requests.get(image_url) 
  
with open(r"C:\Users\DavideSoltys\Desktop\il mio github\Python-Lezione\compiti_22FEBBRARY2023\ChosenSite.html",'w') as f:

    f.write(site.text)

i,k,c = 0,0,0

with open ("ChosenSite.html") as f:
    file = f.read()
    for x in range (len(file)):
        if "img " == file[x:x+4]:
            i = i + 1
        if "class=" == file[x:x+6]:
            k = k + 1
        if "href" == file[x:x+4]:
            c = c + 1

print("Nel file ci sono:")
print(i,"immagini",k,"classi",c,"link") 