import os
from subprocess import call
from time import sleep
from System import System
from User import User
from Admin import Admin
from Student import Student
from Course import Course

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def pause():
    if os.name == 'nt': 
        print ("\nPress any key to continue...")
        _ = os.system("pause")
    elif os.name == 'posix':
        _ = os.system('read -sn 1 -p "\nPress any key to continue..."')

def showadminmenu():
    print(" [2] Add Course")
    print(" [3] Remove Course")
    print(" [4] Logout")
    print(" [5] Exit")

def showstudentmenu():
    print(" [2] Add Course")
    print(" [3] Drop Course")
    print(" [4] View My Cart")
    print(" [5] Logout")
    print(" [6] Exit")

## MAIN ##
system = System()
isrunning = True

while isrunning:
    clear()
    if not system.start():
        isrunning = False
    
    else:
        isactive = True
        while isrunning and isactive:

            pause()
            clear()

            print("HOME MENU\n")
            print(" [1] View Course Offerings")

            if isinstance(system.getcurrentuser(), Admin):
                showadminmenu()
                admindict = {
                    2 : system.getcurrentuser().addcourse,
                    3 : system.getcurrentuser().removecourse,
                    4 : system.logout
                }

            else:
                showstudentmenu()
                studentdict = {
                    2 : system.getcurrentuser().addcourse,
                    3 : system.getcurrentuser().dropcourse,
                    4 : system.getcurrentuser().viewcart,
                    5 : system.logout
                }

            choice = int(input("\nEnter choice: "))
            if isinstance(system.getcurrentuser(), Admin):
                while not(choice >= 1 and choice <= 5):
                    print("Whoops, invalid input!")
                    choice = int(input("\nEnter choice: "))
            else:
                while not(choice >= 1 and choice <= 6):
                    print("Whoops, invalid input!")
                    choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                system.viewcourses()
               
                
            elif isinstance(system.getcurrentuser(), Admin):
                if choice == 2 or choice == 3:
                    admindict[choice](system)
                    
                elif choice == 4:
                    admindict[choice]()
                    isactive = False
                       
                else:
                    isrunning = False

            elif isinstance(system.getcurrentuser(), Student):
                if choice == 2:
                    if len(system.getcourses()) > 0:
                        system.viewcourses()
                        classnum = int(input("\nEnter course number to take: "))

                        while not(classnum >= 1 and classnum <= len(system.getcourses())):
                                print ("Whoops, invalid input!")
                                classnum = int(input("\nEnter course number to take: "))

                        studentdict[choice](system.getcourses()[classnum-1])
                    else:
                        print("\nNo courses to display.")
                    
                    
                elif choice == 3:
                    system.getcurrentuser().viewcart()
                    
                    if len(system.getcurrentuser().getcart()) > 0:
                        classnum = int(input("\nEnter course number to drop: "))
                        while not(classnum >= 1 and classnum <= len(system.getcurrentuser().getcart())):
                                print ("Whoops, invalid input!")
                                classnum = int(input("\nEnter course number to drop: "))
                                
                        studentdict[choice](system.getcurrentuser().getcart()[classnum-1])
                    else:
                        print("Whoops, nothing to remove!")
                    

                elif choice == 4 or choice == 5:
                    studentdict[choice]()
                    
                    if choice == 5:
                        isactive = False

                else:
                    isrunning = False
            
            
        clear()    
            
      
           
  
        

