#Practice

def MainMenu():
    print()
    print("\t\tVehicle Menu")
    print("\tDisplay Cars\t\t1\n","\tAdd/Delete Vehicle\t2")

def menuCalling():
    MainMenu()
    try:
        user=int(input("Enter any option from 1-6:"))

    except ValueError:
        print("Type the correct number.")
        menuCalling()
    
    else:
        if user==1:
        
            def displayCars():
                user=input("""Enter "A" for avaiable cars and "R" for for rented cars:""")
                with open("Vehicle.txt","r") as f1:
                    a=f1.readlines()

                    try:
                        for line in a:
                            lines=line.strip().split(",")

                            if user=="A" and lines[5]=="A" :
                                print(line,end="")

                            if user=="R" and lines[5]=="R":
                                print(line,end="")

                            if user!="A" and user!="R":
                                raise Exception

                    except Exception:
                        menuCalling()

            displayCars()
            menuCalling()

        elif user==2:
            
            def Add_Vehicle():
                vehicle_ID=input("Enter vehicle ID:")
                name=input("Enter name of the vehicle:")
                type=input("""Enter "O" for ordinary and "P" for premium:""")
                try:
                    mileage_allowance=int(input("Enter mileage allowance:"))

                except ValueError:
                    print("Mileage allowance should be only integer value.")
                    menuCalling()
                    
                try:
                    rent_rate=float(input("Enter daily rent rate:"))

                except ValueError:
                    print("Rent rate should only be numberical value.")
                    menuCalling()
                
                status=input("""Enter "A" for available and "R" for rented:""")
    
                with open("Vehicle.txt","a") as f2:
                    f2.write("\n"+vehicle_ID+","+name+","+type+","+str(mileage_allowance)+","+str(rent_rate)+","+status)

                while True:
                    ask=input("Do you want to add one more vehicle? Type y for yes and n for no:")

                    if ask=="y":
                        Add_Vehicle()

                    if ask=="n":
                        break

            def Delete_Vehicle():
                vehicle_ID=input("Enter vehicle ID:")
                list1=[]

                with open("Vehicle.txt","r") as f1:
                    a=f1.readlines()

                    for elements in a:
                        list1.append(elements.strip())
                        
                    for lines in a:
                        line=lines.strip().split(",")

                        if line[0]==vehicle_ID:
                            list1.remove(lines.strip())

                            with open("deletedVehicles.txt","a") as f2:
                                f2.write("\n"+line[0]+","+line[1])

                            with open("Vehicle.txt","w") as f3:
                                for items in list1:
                                    f3.write(items+"\n")

                            with open("Vehicle.txt","a") as f4:
                                f4.write(line[0]+","+"R")



            user=input("Do you want to add or delete a vehicle? Press A for add and D for delete:")
            if user=="A":
                Add_Vehicle()
                menuCalling()

            if user=="D":
                Delete_Vehicle()
                menuCalling()


        elif user==3:
            vehicle_ID=input("Enter vehicle ID:")
            
            
                            

menuCalling()

                
