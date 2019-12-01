class Course:
    name = ""
    code = ""
    units = ""
    limit = ""
    prerequisite = "" # fix
    

class User:
    idnumber = ""
    password = ""

    # name?
    def __init__(self, idnumber, password):
        self.idnumber = idnumber
        self.password = password



class Admin(User):
    #login, create, remove class
    def createCourse(self, course):
        self.


class Student(User):
    # login, take, drop
   