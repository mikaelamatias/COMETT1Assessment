class Course:
    name = ""
    code = ""
    unit = ""
    capacity = ""
    # section, day, time, room, enrolled

    def __init__(self, name, code, unit, capacity):
        self.name = name
        self.code = code
        self.unit = unit
        self.capacity = capacity
        self.prerequisites = []
        self.students = []
    # TODO:

    def getname(self):
            return self.name

    def getcode(self):
        return self.code
    
    def getunit(self):
        return self.unit
    
    def getcapacity(self):
        return self.capacity

    def getprerequisites(self):
        return self.prerequisites
    
    def getstudents(self):
        return self.students

    def isfull (self):
        if (int(self.capacity) == len(self.students)):
            return True
        else:
            return False

    def addprerequisite(self, course):
        self.prerequisites.append(course)  
    
    def removeprerequisite(self, course):
        self.prerequisites.remove(course) 
    
    def addstudent(self, student):
        self.students.append(student)

    def removestudent(self, student):
        self.students.remove(student)
    
    #TODO: prereq done, toString