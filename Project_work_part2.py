#Project work part Two

from datetime import datetime
import matplotlib.pyplot as mp

def vehicleMenu():
    print("\t\tVehicle Menu\n")
    print("\tDisplay Cars\t\t\t\t1\n","\tAdd/deleteVehicle\t\t\t2\n","\tRent Vehicle: Ordinary or Premium\t3\n","\tComplete Rent\t\t\t\t4\n","\tReporting vehicle information\t\t5\n","\tExit\t\t\t\t\t6\n")

def menuCalling():
    vehicleMenu()
    try:
        user_choice=int(input("Choose any option from 1-4:"))
        print()
        
    except ValueError:
        print("Type the correct number.")
        menuCalling()
    
    else:
        if user_choice==1:

            def displayCars():
                
                f1=open("Vehicle.txt","r")
                a=f1.readlines()
                for line in a:
                    print(line.strip())
                f1.close()
                print()

                user_input=input("""Enter "A" to display available vehicles or "R" to display rented vehicles:""")
                try:
                    if user_input=="A":
                        f2=open("Vehicle.txt","r")
                        b=f2.readlines()
                        for i in b:
                            a=i.split(",")
                            if "A" in a[5]:
                                print(i.strip())
                        f2.close()
                        menuCalling()

                    elif user_input=="R":
                        f3=open("Vehicle.txt","r")
                        c=f3.readlines()
                        for j in c:
                            b=j.split(",")
                            if "R" in b[5]:
                                print(j.strip())
                        f3.close()
                        menuCalling()

                    else:
                        raise Exception

                except Exception:
                    print("Type the correct letter.")
                    menuCalling()
                    

            displayCars()


        if user_choice==2:
            user=input("""Enter "A" for adding vehicle and "D" for deleting vehicle:""")

                
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

                f4=open("Vehicle.txt","a")
                f4.write("\n"+vehicle_ID+','+name+','+type+','+str(mileage_allowance)+','+','+str(rent_rate)+','+status)
                f4.close()

            
                while True:
                    user_wish=input("Do you want to continue adding vehicles? Type y for yes and n for no:")

                    if user_wish=="y":
                        print()
                        Add_Vehicle()

                    elif user_wish=="n":
                        break
                
                menuCalling()


            def Delete_Vehicle():
                vehicle_ID=input("Enter vehicle ID:")
                
                with open("Vehicle.txt","r") as f5:
                    lines=f5.readlines()
                    
                for line in lines:
                    d=line.strip().split(",")
                         
                    if vehicle_ID == d[0]:
                        with open("deletedVehicles.txt","a") as f6:
                            f6.write("\n"+line)

                            with open("Vehicle.txt","r+") as f:
                                new_f=f.readlines()
                                f.seek(0)
                                for line in new_f:
                                    if vehicle_ID not in line:
                                        f.write(line)
                                f.truncate()
                                break
                            
                if vehicle_ID!=d[0]:
                    print("The vehicle ID was not found. Please check vehicle ID.")
                    menuCalling()
            

                while True:
            
                    user_wish=input("Do you want to delete another vehicle info? Type y for yes and n for no:")

                    if user_wish=="y":
                        Delete_Vehicle()
                        break

                    elif user_wish=="n":
                        menuCalling()
                        break
                            
            if user=="A":
                Add_Vehicle()

            if user=="D":
                Delete_Vehicle()
                        
        if user_choice==3:
            
            accessories=['GPS navigator','Built-in mini fridge','car additional seat']
            now=datetime.now()
            starting_date_time=now.strftime("%d/%m/%Y %H:%M")

            def rentDetails(information):
                with open("rentVehicle.txt","a") as f8:
                    f8.write(information)
            
            def rentVehicle(vehicleID):
                f7=open("Vehicle.txt","r")
                a=f7.readlines()
                list2=[]
                list1=[]
                f7.close()
                for i in a:
                    list2.append(i.strip())
                
                for k in a:
                    b=k.strip().split(",")
                    
                    if vehicleID == b[0] and "A" in b[5] and "P" in b[2]:
                        renterID=input("Enter your social security number:")
                        
                        try:
                            odometer=int(input("Enter odometer reading of the vehicle:"))
                            
                        except ValueError:
                            print("Odometer should only be an integer value.")
                            menuCalling()
                            break
                            
                        print("Car details:",b,"\n")
                        print("\tAdditional accessories for premium type cars:")

                        for items in list2:
                            if vehicleID in items:
                                list2.remove(items)

                                with open("Vehicle.txt","w") as f:
                                    for element in list2:
                                        f.write(element+"\n")

                                with open("Vehicle.txt","a") as f1:
                                        f1.write(b[0]+','+b[1]+','+b[2]+','+b[3]+','+b[4]+','+"R")
                                        
                                
                            
                        for i in accessories:
                            print(i)

                        list1=[]
                        while True:
                            ask=input("Do you want additional accessories? Type y for yes and n for no:")
                            if ask=="y":
                                try:
                                    selection=int(input("Press 1 for GPS navigator, Press 2 for Buil-in minifridge, Press 3 for car additional seat:"))

                                except ValueError:
                                    print("Please choose either 1 or 2 or 3.")
                                    continue

                                if selection ==1:
                                    list1.append(accessories[0])

                                elif selection==2:
                                    list1.append(accessories[1])

                                elif selection ==3:
                                    list1.append(accessories[2])

                                else:
                                    menuCalling()

                            elif ask=="n":
                                break

                        print("Additional accessories bought:",list1)
                        print("Car",vehicleID,"is rented to",renterID,"\n")
                        print("*"*20,"Vehicle Details","*"*20,"\n")

                        if len(list1)==0:
                            print("vehicle ID=",vehicleID,"|Description=",b[1],"|Daily Rate=",b[4],"|accessories=0 |Status=R |Renter ID=",renterID,"|Date/time of rent=",starting_date_time,"|rent starting odometer=",odometer)

                            rent_info="\n"+str(vehicleID)+','+str(renterID)+','+str(starting_date_time)+','+str(odometer)
                            rentDetails(rent_info)
                            print("Renting vehicle is successful")
                            menuCalling()

                        elif len(list1) !=0:
                            print("vehicle ID=",vehicleID,"|Description=",b[1],"|Daily Rate=",b[4],"|accessories=20 |Status=R |Renter ID=",renterID,"|Date/time of rent=",starting_date_time,"|rent starting odometer=",odometer)
                
                            rent_info="\n"+str(vehicleID)+','+str(renterID)+','+str(starting_date_time)+','+str(odometer)+','+str(list1)
                            rentDetails(rent_info)
                            print("Renting vehicle is successful")
                            menuCalling()

                    elif vehicleID == b[0] and "R" in b[5]:
                        print("The vehicle is on rent.")
                        menuCalling()

                if vehicleID!=b[0]:
                    print("The vehicle is not available. Please check the vehicleID and the staus of availability.")
                    menuCalling()
                    
            vehicle_ID=input("Enter vehicle ID:")
            rentVehicle(vehicle_ID)

        if user_choice==4:
            
            now=datetime.now()
            date_time=now.strftime("%d/%m/%Y %H:%M")
            ending_date_time=datetime.strptime(date_time,"%d/%m/%Y %H:%M")
            list3=[]
            list4=[]

            def transactionDetails(information):
                with open("Transactions.txt","a") as f9:
                    f9.write(information)
            
            def RentComplete(vehicleID):
                
                with open("Vehicle.txt","r") as f1:
                    a=f1.readlines()

                    for i in a:
                        list4.append(i.strip())

                    for line in a:
                        info=line.strip().split(",")

                        if info[0]==vehicleID and "R" in info[5]:

                                with open("rentVehicle.txt","r") as f2:
                                    b=f2.readlines()
                                        
                                    for line in b:
                                        element=line.strip().split(",")
                                    
                                        if element[0]==vehicleID:
                                            for i in element:
                                                list3.append(i.strip())
                                            start_date=element[2]
                                            starting_date_time=datetime.strptime(start_date,"%d/%m/%Y %H:%M")
                                            rent_start_odometer=element[3]
                                    
                                renterID=input("Enter your social security number:")
                                try:
                                    rent_end_odometer=int(input("Enter odometer reading of the vehicle:"))

                                    if rent_end_odometer<int(rent_start_odometer):
                                        raise Exception
                                    
                                except ValueError:
                                    print("Odomoter should only be an integer value.")
                                    menuCalling()
                                    break

                                except Exception:
                                    print("Rent ending odomoter should be bigger than rent starting odometer.")
                                    menuCalling()
                                    break
                        
                                number_of_days=abs((ending_date_time-starting_date_time).days)+1
                                kilometers_driven=rent_end_odometer-int(rent_start_odometer)
                                chargeable_kilometers=kilometers_driven-((number_of_days)*(float(info[3])))

                                for items in list4:
                                    if vehicleID in items:
                                        list4.remove(items)

                                with open("Vehicle.txt","w") as f:
                                    for element in list4:
                                        f.write(element+"\n")

                                with open("Vehicle.txt","a") as f1:
                                        f1.write(info[0]+','+info[1]+','+info[2]+','+info[3]+','+info[4]+','+"A")
                                        

                                if len(list3)>5:
                                    rental_charge=(float(info[4])*number_of_days)+(number_of_days*20)+(chargeable_kilometers*0.025)
                                    print("Car",vehicleID,"is returned from",renterID,"\n")
                                    print("*"*20,"Vehicle Details","*"*20,"\n")
                                    print("vehicle ID=",vehicleID,"|Description=",info[1],"|Daily Rate=",info[4],"|accessories=20 |Renter ID=",renterID,"|Date/time of return=",date_time,"|rent starting odometer=",rent_start_odometer,"|rent end odometer=",rent_end_odometer,"|Kms.run=",kilometers_driven,"|Rental charges=",rental_charge)
                                    transactions_info="\n"+str(vehicleID)+','+str(renterID)+','+str(date_time)+','+str(rent_start_odometer)+','+str(rent_end_odometer)+','+str(rental_charge)
                                    transactionDetails(transactions_info)
                                    print("Car",vehicleID,"is returned")
                                    menuCalling()
                                    break

                                else:
                                    rental_charge=(float(info[4])*number_of_days)+(chargeable_kilometers*0.025)
                                    print("Car",vehicleID,"is returned from",renterID,"\n")
                                    print("*"*20,"Vehicle Details","*"*20,"\n")
                                    print("vehicle ID=",vehicleID,"|Description=",info[1],"|Daily Rate=",info[4],"|accessories=0 |Renter ID=",renterID,"|Date/time of return=",date_time,"|rent starting odometer=",rent_start_odometer,"|rent end odometer=",rent_end_odometer,"|Kms.run=",kilometers_driven,"|Rental charges=",rental_charge)
                                    transactions_info="\n"+str(vehicleID)+','+str(renterID)+','+str(date_time)+','+str(rent_start_odometer)+','+str(rent_end_odometer)+','+str(rental_charge)
                                    transactionDetails(transactions_info)
                                    print("Car",vehicleID,"is returned")
                                    menuCalling()
                                    break
                            
                    if vehicleID!=info[0] or "A" in info[5]:
                        print("The vechile do not exist in our system. Please check the vehicle ID.")
                        menuCalling()

            vehicle_ID=input("Enter vehicle ID:")                    
            RentComplete(vehicle_ID)

        if user_choice==5:
            try:
                user=int(input("Enter 1 to see the number of vehicles of each type or 2 to see the income earned in last 3 months:"))

            except ValueError:
                print("Type the correct number.")
                menuCalling()

            else:
                
                if user==1:
                    count_ordinary=0
                    count_premium=0
                    
                    with open("Vehicle.txt","r") as f:
                        line=f.readlines()
                        for a in line:
                            i=a.strip().split(",")
                            
                            if i[2]=="O":
                                count_ordinary+=1

                            elif i[2]=="P":
                                count_premium+=1
                                
                    xnames=["Ordinary","Premium"]
                    ynumber=[count_ordinary,count_premium]
                    mp.xlabel("Type of vehicle")
                    mp.ylabel("Number of vehicles")
                    mp.bar(xnames,ynumber,color='maroon',width=0.5)
                    mp.show()

                if user==2:
                    list1=[]
                    with open("Transactions.txt","r") as f1:
                        a=f1.readlines()

                        for b in a:
                            c=b.strip().split(",")
                            list1.append(c[5])
                        
                        sales_January=float(list1[0])+float(list1[1])+float(list1[2])+float(list1[3])+float(list1[4])
                        sales_February=float(list1[5])+float(list1[6])+float(list1[7])+float(list1[8])
                        sales_March=float(list1[9])+float(list1[10])+float(list1[11])+float(list1[12])
                        sales_April=float(list1[13])+float(list1[14])+float(list1[15])+float(list1[16])

                        with open("MonthlySales.txt","w") as f2:
                            f2.write("January:"+str(sales_January)+"\n"+"February:"+str(sales_February)+"\n"+"March:"+str(sales_March)+"\n"+"April:"+str(sales_April))

                        with open("MonthlySales.txt","r") as f3:
                            sales={}
                            for info in f3:
                                a=info.split(":")
                                sales.update({a[0]:float(a[1].strip())})

                            xpoints=sales.keys()
                            ypoints=sales.values()
                            mp.plot(xpoints,ypoints,color='maroon',marker='o')
                            mp.xlabel("Months")
                            mp.ylabel("Sales")
                            mp.grid(color='r',linestyle='dashed')
                            mp.show()
                                
        if user_choice==6:
                print("Thanks for using Car Rental System. Bye! Bye!")
            
menuCalling()        

                
            


        

