class User:
    idnumber = ""
    password = ""

    def __init__(self, idnumber, password):
        self.idnumber = idnumber
        self.password = password
    
    def getIDnumber(self):
        return self.idnumber
    
    def getpassword(self):
        return self.password
