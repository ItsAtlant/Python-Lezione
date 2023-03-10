#classe rettangolo
#altezza e lunghezza definiti come numero di caratteri disegno 
# disegnare con | _

class Rettangolo():
    def __init__(self,altezza,larghezza):
        self.altezza = altezza
        self.larghezza = larghezza
    
    def costruisci(self):
        spazio = ""
        underscore,upperscore = " ", " "
            
        for x in range(self.larghezza):
            spazio = spazio + "  "
            upperscore = upperscore + "‾ "
            underscore = underscore + "_ "
        print(underscore)
        for x in range(self.altezza):
            print("|"+spazio+"|")
        print(upperscore)

Miorettangolo = Rettangolo(5,20)
Miorettangolo.costruisci()

Rettangolo(20,20).costruisci()