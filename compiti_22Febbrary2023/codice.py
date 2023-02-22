
import requests

image_url = input("Inserisci il link: ")
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("C:\Users\DavideSoltys\Desktop\il mio github\Python-Lezione\compiti_22FEBBRARY2023\ChosenSite.html",'w') as f:

    f.write(r.content)