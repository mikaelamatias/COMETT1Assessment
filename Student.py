from User import User

class Student(User):
    # login, take, drop

    def __init__(self, idnumber, password):
        super().__init__(idnumber, password)
        self.cart = []
        self.totalunits = ""
 
    def addcourse(self, course):
        if course in self.cart:
            print("This class is already in your cart.")
        elif course.isfull():
            print("Whoops, this class is full!")
        else:
            isconflict = False

            for i in range(0, len(self.getcart())):
                if (self.getcart()[i].getday() == course.getday().casefold()) and (self.getcart()[i].gettime() == course.gettime()):
                    print("Whoops, there seems to be a conflict in schedule!")
                    isconflict = True
            
            if not isconflict:
                self.cart.append(course)
                course.addstudent(self)
                print("\n" + course.getcode() + " has been successfully added to your cart.")

    def dropcourse(self, course):
        self.cart.remove(course)
    
    def getcart(self):
        return self.cart
    
    def gettotalunits(self):
        count = 0
        for course in self.cart:
            count += (float)(course.unit)
        self.totalunits = count
        
        return self.totalunits

    def viewcart(self):  
        if (len(self.cart) == 0):
            print ("There are no classes in your cart yet.")
        else:
            print("\nMY CART\n")
            print("\n\tCOURSE CODE\t\t" + "SECTION\t\t" + "NO. OF UNITS\t\t" + "DAYS\t\t" + "TIME\t\t" + "VENUE\t\t" + "ENROLLED\t\t" + "PREREQUISITES")
            for i in range(0, len(self.getcart())):
                print(f"[{i+1}]" + str(self.getcart()[i]))
            
            print("\nTotal units: " + str(self.gettotalunits()))

