from Admin import Admin
from Student import Student

class System:
    courses = []
    users = []
    currentuser = ""
    
    def login(self, idnumber, password, index):
        if self.users[index].getpassword() == password:
            self.currentuser = self.users[index]
            return True
        else:
            return False

    def logout(self):
        self.currentuser = ""
        self.start()
    
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
        if (len(self.courses)) == 0:
            print ("No classes to display.")
        
        else:
            for i in range(0, len(self.courses)):
                print ("\t\t[",(i+1),"] ", self.classes[i])
                
    def start(self):
        print("[1] Register")
        print("[2] Login")
        
        choice = input("\nEnter choice: ")

        while not (choice == '1' or choice == '2'):
            print("ERROR: Invalid input. Please try again.")
            choice = input("\nEnter choice: ")
        
        idnumber = input("ID number: ")
        password = input("Password: ")

        isfound = False
        index = -1
        for i in range(0, len(self.users)):
            if (self.users[i].getIDNumber() == idnumber):
                isFound = True
                index = i

        if choice == '2':
            if not isfound:
                print("Sorry, you are not yet registered.")
                choice == '1'
                #TODO: proceed
            else:
                while not self.login(idnumber, password, index):
                    print ("\nYour ID number and password do not match.")
                    password = input ("Retype password: ") #FIXME: END LOOP
            
                print ("Login successful!")
        
        if choice == '1':
            if isfound:
                print("You are already registered.")
            else:
                print("USER TYPE")
                print(" [A] Admin")
                print(" [S] Student")
            
                usertype = input("\nEnter user type: ")
                
                while not(usertype == 'A' or usertype == 'S'):
                    print ("ERROR: Invalid Input. Please try again.")
                    usertype = input("\nEnter user type: ")
                
                if (usertype == 'A'):
                    user = Admin(idnumber, password)
                elif (usertype == 'S'):
                    user = Student(idnumber, password)
        