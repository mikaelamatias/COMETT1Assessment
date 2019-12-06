from User import User
from Course import Course

class Admin(User):

    def addcourse(self, system):
        name = input("Course name: ")
        code = input("Course code: ")
        unit = input("Number of units: ")
        capacity = input("Maximum capacity: ")
        
        course = Course(name, code, unit, capacity)
        
        hasprereq = True
        while hasprereq:
            res = input("Does this course have any prerequisites? (y/n) : ")

            while not(res.lower() == 'y' or res.lower() == 'n'):
                print("ERROR: Invalid input. Please try again.")
                res = input("Does this course have any prerequisites? (y/n) : ")
            
            if res.lower() == 'y':
                count = input("How many? : ")
                if (int)(count) > 0:
                    for i in range(0, count):
                        prereqcode = input("Course code: ")
                        course.addprerequisite(prereqcode)
                else:
                    res = 'n'
            
            if res.lower() == 'n':
                hasprereq = False

        system.addcourse(course)
    
    def removecourse(self, system):
        system.viewcourses()
        choice = input("\nEnter course number to delete: ")
        
        while not((int)(choice) >= 1 and choice <= len(system.getcourses())):
            print("ERROR: Invalid input. Please try again.")
            choice = input ("\nEnter course number to delete: ")
        
        system.removeclass(system.getclasses()[(int)(choice)-1])

            
            

        
        