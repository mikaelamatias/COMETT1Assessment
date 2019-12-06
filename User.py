class User:
    idnumber = ""
    password = ""

    # create user
    def __init__(self, idnumber, password):
        self.idnumber = idnumber
        self.password = password
    
    def getIDNumber(self):
        return self.idnumber
    
    def getpassword(self):
        return self.password
