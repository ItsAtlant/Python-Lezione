
# imported the requests library
import requests

image_url = input("Inserisci il link: ")
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open(r"C:\Users\DavideSoltys\Desktop\il mio github\Python-Lezione\compiti_22FEBBRARY2023\ChosenSite.html",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)

i = 0
with open ("ChosenSite.html", encoding="utf8") as f:
    file = f.read()
    try:
        for x in range (len(file)):
            if "img " == file[x] + file[x+1] + file[x+2] + file[x+3]:
                i = i + 1
    except:
        print("")
print("Nel file c'è scritto ",i," volte img")