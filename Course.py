class Course:
    name = ""
    code = ""
    section = ""
    unit = ""
    capacity = ""
    day = ""
    time = ""
    venue = ""
    
    def __init__(self, name, code, section, unit, capacity, day, time, venue):
        self.name = name
        self.code = code
        self.section = section
        self.unit = unit
        self.capacity = capacity
        self.day = day
        self.time = time
        self.venue = venue
        self.prerequisites = []
        self.students = []

    def getname(self):
            return self.name

    def getcode(self):
        return self.code
    
    def getsection(self):
        return self.section

    def getunit(self):
        return self.unit
    
    def getcapacity(self):
        return self.capacity
    
    def getday(self):
        return self.day

    def gettime(self):
        return self.time

    def getvenue(self):
        return self.venue

    def getprerequisites(self):
        return self.prerequisites
    
    def getstudents(self):
        return self.students

    def isfull (self):
        if (int(self.capacity) == len(self.students)):
            return True
        else:
            return False

    def addprerequisite(self, code):
        self.prerequisites.append(code)  
    
    def removeprerequisite(self, code):
        self.prerequisites.remove(code) 
    
    def addstudent(self, student):
        self.students.append(student)

    def removestudent(self, student):
        self.students.remove(student)
    
    def __str__ (self):

        string = "\t" + self.getcode() + "\t\t\t" + self.getsection() + "\t\t" + str(self.getunit()) 
        string += "\t\t\t" + self.getday() + "\t\t" + self.gettime() + "\t" + self.getvenue() 
        string += "\t\t" + str(len(self.getstudents())) + "/" + str(self.getcapacity()) + "\t\t\t"
        
        for i in range(0, len(self.getprerequisites())):
            string += self.getprerequisites()[i] + " "
        
        return string