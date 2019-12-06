from System import System
from User import User
from Admin import Admin
from Student import Student
from Course import Course

def showadminmenu():
    print(" [2] Add Course")
    print(" [3] Remove Course")
    print(" [4] Logout")
    print(" [5] Exit")

def showstudentmenu():
    print(" [2] Add Course")
    print(" [3] Drop Course")
    print(" [4] View Cart")
    print(" [5] Logout")
    print(" [6] Exit")

## MAIN ##
system = System()
isactive = True

while isactive:
    
    system.start()
    
    print("HOME")
    print(" [1] View Course Offerings")

    if isinstance(system.getcurrentuser(), Admin):
        showadminmenu()
        admindict = {
            2 : system.getcurrentuser().addcourse,
            3 : system.getcurrentuser().removecourse,
            4 : system.getcurrentuser().logout()
        }

    else:
        showstudentmenu()
        studentdict = {
            2 : system.getcurrentuser().addcourse,
            3 : system.getcurrentuser().removecourse,
            4 : system.getcurrentuser().viewcart(),
            5 : system.getcurrentuser().logout()
        }

    choice = input("Enter choice: ")
    if isinstance(system.getcurrentuser(), Admin):
        while not(choice >= '1' and choice <= '4'):
            print("ERROR: Invalid input. Please try again.")
            choice = input("Enter choice: ")
    else:
        while not(choice >= '1' and choice <= '5'):
            print("ERROR: Invalid input. Please try again.")
            choice = input("Enter choice: ")
    
    #TODO: 1
    if isinstance(system.getcurrentuser(), Student):
        if choice == '2':
            if len(system.getcourses()) > 0:
                system.viewcourses()
                classnum = input("\nEnter class number: ")
                while not(classnum >= '1' and classnum <= str(len(system.getcourses()))):
                        print ("ERROR: Invalid Input. Please try again.")
                        classnum = input("\nEnter class number: ")
                studentdict[int(choice)](system.getcourses()[int(classnum)-1])
            else:
                print("No course offerings to display.")

        elif choice == '3':
            system.getcurrentuser().viewcart()
            
            if len(system.getcurrentuser().viewcart()) > 0:
                classnum = input("\nEnter class number: ")
                while not(classnum >= '1' and classnum <= str(len(system.getcurrentuser().getcart()))):
                        print ("ERROR: Invalid Input. Please try again.")
                        classnum = input("\nEnter class number: ")
                studentdict[int(choice)](system.getcourses()[int(classnum)-1])
        
        elif choice != '6':
            studentdict[int(choice)]()

        elif choice == '6':
            isactive = False
           
    elif isinstance(system.getcurrentuser(), Admin):
        if choice == '2' or choice == '3':
            admindict[int(choice)](system)

        elif choice == '4':
            admindict[int(choice)]
            
        elif choice == '5':
            isactive = False
        

