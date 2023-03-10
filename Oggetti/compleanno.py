#calcolo eta
from datetime import time
print(time())
class Dipendete():
    def __init__(self, nome, codice_fiscale, indirizzo, stipendio):
        self.nome = nome
        self.codice_fiscale = codice_fiscale
        self.indirizzo = indirizzo
        self.stipendio = stipendio
    
    def __set_nome__(self,nome):
        self.nome = nome
    def __get_nome__(self):
        return self.nome
    
    def __set_codice_fiscale__(self,codice_fiscale):
        self.codice_fiscale = codice_fiscale
    def __get_codice_fiscale__(self):
        return self.codice_fiscale
    
    def __set_indirizzo__(self,indirizzo):
        self.indirizzo = indirizzo
    def __get_indirizzo__(self):
        return self.indirizzo
    
    def __set_stipendio__(self,stipendio):
        self.stipendio = stipendio
    def __get_stipendio__(self):
        return self.stipendio

Nicolo = Dipendete("Nicolo","BCKDWHABFO213B","ViaRossini16",92318091487109284091)

print(Nicolo.__get_stipendio__())