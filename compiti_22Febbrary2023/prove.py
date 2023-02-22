
import requests

image_url = input("Inserisci il link: ")
  

r = requests.get(image_url) 
  
with open(r"C:\Users\DavideSoltys\Desktop\il mio github\Python-Lezione\compiti_22FEBBRARY2023\ChosenSite.html",'wb') as f:

    f.write(r.content)

i = 0
k = 0 
c = 0
with open ("ChosenSite.html", encoding="utf8") as f:
    file = f.read()
    try:
        for x in range (len(file)):
            if "img " == file[x] + file[x+1] + file[x+2] + file[x+3]:
                i = i + 1
            if "class=" == file[x] + file[x+1] + file[x+2] + file[x+3] + file[x+4] + file[x+5]:
                k = k + 1
            if "https" == file[x] + file[x+1] + file[x+2] + file[x+3] + file[x+4]:
                c = c + 1
    except:
        print("")
print("Nel file ci sono:")
print(i,"immagini",k,"classi",c,"link") 