from Admin import Admin
from Student import Student

class System:
    courses = []
    users = []
    currentuser = ""
    
    def login(self, idnumber, password, index):
        if (self.users[index].getIDnumber() == idnumber) and (self.users[index].getpassword() == password):
            self.currentuser = self.users[index]
            return True
        else:
            return False

    def logout(self):
        self.currentuser = ""
    
    def getusers(self):
        return self.users

    def getcurrentuser(self):
        return self.currentuser
    
    def getcourses(self):
        return self.courses

    def adduser(self, user):
        self.users.append(user)
    
    def addcourse(self, course):
        self.courses.append(course)
    
    def removecourse(self, course):
        self.courses.remove(course)

    def viewcourses(self):    
        if (len(self.getcourses())) == 0:
            print ("\nNo courses to display.")
        
        else:
            print("\nCOURSE OFFERINGS\n")
            print("\n\tCOURSE CODE\t\t" + "SECTION\t\t" + "NO. OF UNITS\t\t" + "DAYS\t\t" + "TIME\t\t" + "VENUE\t\t" + "ENROLLED\t\t" + "PREREQUISITES")
            for i in range(0, len(self.getcourses())):
                print(f" [{i+1}]" + str(self.getcourses()[i])) 
    
    def showlogo(self):
        print("            (_)       ")                        
        print("  __ _ _ __  _ _ __ ___   ___   ___ _   _ ___") 
        print(" / _` | '_ \| | '_ ` _ \ / _ \ / __| | | / __|")
        print("| (_| | | | | | | | | | | (_) |\__ \ |_| \__ \\")
        print(" \__,_|_| |_|_|_| |_| |_|\___(_)___/\__, |___/")
        print("                                     __/ |    ")
        print("                                    |___/     ")
            
    def start(self):
        self.showlogo()
        print("\n [1] Register")
        print(" [2] Login")
        print(" [3] Exit")
    
        choice = int(input("\nEnter choice: "))

        while not (choice >= 1 and choice <= 3):
            print("Whoops, invalid input!")
            choice = int(input("\nEnter choice: "))
        

        if choice == 3:
            return False

        else: 
            idnumber = input("\nID number: ")
            password = input("Password: ")

            isfound = False
            index = -1
            for i in range(0, len(self.getusers())):
                if (self.getusers()[i].getIDnumber() == idnumber):
                    isfound = True
                    index = i
            
            if choice == 2:
                if not isfound:
                    print("\nYou are not yet registered. Please provide the following information to register.")
                    choice = 1
                else:
                    while not self.login(idnumber, password, index):
                        print ("\nWhoops, your ID number and password do not match!")
                        idnumber = input("\nID number: ")
                        password = input("Password: ")
                
                    print("\nLogin successful!")
                    
            if choice == 1:
                if isfound:
                    print("\nYou are already registered.")
                    while not self.login(idnumber, password, index):
                        print ("\nWhoops, your ID number and password do not match!")
                        idnumber = input("\nID number: ")
                        password = input("Password: ")
                    
                    print("Login successful!")
                else:
                    usertype = input("User type (a/s): ")
                        
                    while not(usertype.casefold() == 'a' or usertype.casefold() == 's'):
                        print ("Whoops, invalid input!")
                        usertype = input("\nReenter user type: ")
                        
                    if (usertype.casefold() == 'a'):
                        user = Admin(idnumber, password)
                    elif (usertype.casefold() == 's'):
                        user = Student(idnumber, password)
                    
                    self.adduser(user)
                    index = len(self.getusers()) - 1
                    self.login(idnumber, password, index)
            
            return True
            
        
        