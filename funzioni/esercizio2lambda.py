lista = ["Ciao","Come","stai","Signore"]
Stampante = list(filter(lambda x: x[0].isupper(), lista))
print(Stampante)