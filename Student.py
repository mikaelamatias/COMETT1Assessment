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
            print("Sorry, this class is full!")
        else:
            self.cart.append(course)
            course.addstudent(self)
            print(course.getcode() + " has been successfully added to your cart.")

    def dropcourse(self, course):
        self.cart.remove(course)
    
    def getcart(self):
        return self.cart
    
    def gettotalunits(self):
        count = 0
        for course in self.cart:
            count += (int)(course.unit)
        self.totalunits = count
        
        return self.totalunits

    def viewcart(self):  
        if (len(self.cart) == 0):
            print ("There are no classes in your cart yet.")
        else:
            for i in range(0, len(self.cart)):
                print ("\t\t[",(i+1),"] ", self.cart[i])
            # print("Total Units: " + self.gettotalunits())

