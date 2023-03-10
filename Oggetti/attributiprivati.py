class Student():
    def __init__(self,firts,last,eta):
        self.__nome = firts
        self.__cognome = last
        self.__eta = eta

    def getNome(self):

        return self.__nome
    
    def setAge(self,eta):

        self.eta = eta/2
    

studente = Student("Marco","soltys",20)
nominativo = studente.getNome() 
print(nominativo,studente.setAge(505050523034))

