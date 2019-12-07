from User import User
from Course import Course

class Admin(User):

    def addcourse(self, system):
        name = input("\nCourse name: ")
        code = input("7-character course code: ")
        section = input("Section: ")

        while True:
            try:
                unit = float(input("Number of units: "))
                if unit >= 0:
                    break
            except:
                print("\mWhoops, invalid input!\n")
                pass

        while True:
            try:
                capacity = int(input("Maximum capacity: "))
                if capacity >= 0:
                    break
            except:
                print("\nWhoops, invalid input!\n")
                pass
            
        day = input("Days (ex. MW, TH): ")
        time = input("Time (ex. 0730-0900): ")
        venue = input("Venue: ")

        isconflict = False

        for i in range(0, len(system.getcourses())):
                if (system.getcourses()[i].getcode() == code.casefold()) and (system.getcourses()[i].getsection() == section.casefold()):
                    print("\nWhoops, this course has already been added to the system!")
                    isconflict = True
        
        if not isconflict:
            course = Course(name, code, section, unit, capacity, day, time, venue)
            
            hasprereq = True
            while hasprereq:
                res = input("Does this course have any prerequisites? (y/n) : ")

                while not(res.casefold() == 'y' or res.casefold() == 'n'):
                    print("Whoops, invalid input!")
                    res = input("\nDoes this course have any prerequisites? (y/n) : ")
                
                if res.casefold() == 'y':
                    count = input("How many? : ")
                    try:
                        count = int(count)
                        if count > 0:
                            for i in range(count):
                                prereqcode = input("7-character course code: ")
                                if not prereqcode.casefold() == course.getname():
                                    course.addprerequisite(prereqcode)
                            hasprereq = False
                        else:
                            res = 'n'
                    except ValueError:
                        print("\nWhoops, invalid input! Let's start over.\n")
                
                if res.casefold() == 'n':
                    hasprereq = False

            system.addcourse(course)
            print("\nCourse added successfully.")
    
    def removecourse(self, system):
        system.viewcourses()
        if len(system.getcourses()) > 0:
            choice = int(input("\nEnter course number to delete: "))
            
            while not(choice >= 1 and choice <= len(system.getcourses())):
                print("Whoops, invalid input!")
                choice = int(input("\nEnter course number to delete: "))
            
            system.removecourse(system.getcourses()[choice-1])
            print("\nCourse removed successfully.")
        

            
            

        
        