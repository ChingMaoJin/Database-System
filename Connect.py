#importing the libraries needed for the program
import mysql.connector
import time
import os

# The passcode and username must not be hardcoded
username=input("Please enter the username of your mysql server: ")
passcode=input("Please enter your password to connect to your mysql server: ") 

#creating an object to connect to mysql server with the hostname, username, password and database name provided
mydb = mysql.connector.connect(
  host="localhost",
  user=username,
  password=passcode,
  database="ChingMaoJin_22013213"
)

mycursor = mydb.cursor() #Create a cursor object to execute sql query
print("You have connected to the mysql server successfully! Yay!!!") #assuring the user has successfully connected to the server
input("Please press enter key to continue ...")
i=0
while i!=5:
    os.system("clear")
    #creating an interactive menu for the user
    print("Welcome to the database front end")
    print("1)Execute already defined query")
    print("2)Insert a new data")
    print("3)Update a new data")
    print("4)Delete a new data")
    print("5)Exit")
    i=int(input("Your choice: "))
    if i==1: #Execute previously defined query
        Choice=0
        while Choice !=15:
            os.system("clear") #clear the screen before showing the menu
            #displaying the pre-defined ques to the users for execution
            print("Which query do you want to execute")
            print("1: What is the coach name of the athelete")
            print("2: What are the male athletes")
            print("3: What is the event time for all types of football match")
            print("4: What are the athletes that are included in the medallists")
            print("5: What are the athletes that awarded gold medal")
            print("6: What is the coach for football")
            print("7: What is the venue for badminton")
            print("8: What is the event date for football")
            print("9: What are the athletes that are not in the medallists")
            print("10: Group the athlete based on the same sport and display the column number of athlete and sport")
            print("11: How many events takes place between 2024-8-20 to 2024-9-20")
            print("12: Total numbers of athletes that are not in the medallists")
            print("13: Find the average age of the athletes of each sport")
            print("14: Display the athletes who are taking the sport and the sport")
            print("15: Exit")
            Choice=int(input("Your choice: "))
            if Choice==1:
              mycursor.execute("select Coach_Name from Athlete;") #executing the sql query to MySQL
              result=mycursor.fetchall() #fetching all the result after execution to display to the users
              for row in result:  #iterate through the result and print each row of result
                  print(f"CoachName: {row[0]}") #format the String displayed
              print(mycursor.rowcount, "rows.") #telling the user of the total number of rows
              input("Please press enter key to continue ...") #Giving user time to view the result before preceeding

            elif Choice==2:
              mycursor.execute("select Athlete_Name,Athlete_ID, gender from Athlete where gender='M' order by(Athlete_ID) desc;") #executing the sql query to MySQL
              result=mycursor.fetchall() #fetching all the result after execution to display to the users
              for row in result: #iterate through the result and print each row of result
                  print(f"AthleteName: {row[0]}, AthleteID: {row[1]}, Gender: {row[2]}.") #format the String displayed
                  print(row[0] + " , " + str(row[1]) + " , " + row[2])
              print(mycursor.rowcount, "rows.")  #telling the user of the total number of rows
              input("Please press enter key to continue ...") #Giving user time to view the result before preceeding

            
            elif Choice==3:
            #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
              mycursor.execute("select Event_Time, Sport from Event where Sport Like '%football%';") 
              result=mycursor.fetchall()
              for row in result:
                  print(f"Event time: {row[0]}, Sport: {row[1]}.")
              print(mycursor.rowcount, "rows.")
              input("Please enter key to continue ...")
              
            elif Choice==4:
            
                sql="""Select A.Athlete_Name, M.Medal_Place from Athlete A LEFT OUTER JOIN Medallist M
                        on A.Athlete_ID=M.Athlete_ID
                        where M.Athlete_ID IS NOT NULL;""" #triple double quotation means multi line of String
                        
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                mycursor.execute(sql) 
                result=mycursor.fetchall()
                for row in result:
                    print(f"AthleteName:{row[0]}, Medal_Place:{row[1]} ")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
            
            elif Choice==5:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select A.Athlete_Name, M.Medal_Place, M.Athlete_ID from Athlete As A inner join 
                        (select Medal_Place, Athlete_ID from Medallist where Medal_Place=1) as M
                        on M.Athlete_ID=A.Athlete_ID
                        order by(M.Athlete_ID) desc;"""
                mycursor.execute(sql) #execute the sql query on mysql server
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"AthleteName:{row[0]}, Medal_Place:{row[1]}, Athlete_ID:{row[2]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==6:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select Coach_Name, Sport from Coach
                        where Sport like '%football%';"""
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"CoachName:{row[0]}, Sport:{row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==7:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="select Venue_Name, Sport from Venue where Sport='Badminton';"
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"VenueName:{row[0]}, Sport:{row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==8:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select Date_Format(Start_Date, '%e %M %Y') as Event_Date, Sport from Event
                        where Sport like '%football%';"""
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"Event_Name:{row[0]}, Sport:{row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==9:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select A.Athlete_Name, A.Athlete_ID from Athlete as A left outer join Medallist as M 
                        on A.Athlete_ID=M.Athlete_ID
                        where M.Athlete_ID is null;"""
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"AthleteName:{row[0]}, Athlete_ID:{row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==10:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="select Count(Athlete_Name) as Num_of_Athletes, Sport from Athlete Group by (Sport);"
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"NumOfAthletes:{row[0]}, Sport:{row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
            
            elif Choice==11:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select Count(Sport) as Num_Of_Events from Event
                    where Start_Date between '2024-08-20' and '2024-09-20';"""
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"NumOfEvents:{row[0]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==12:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select count(A.Athlete_ID) as number_of_Athletes_not_on_medalList from Athlete as A left outer join Medallist as M
                        on A.Athlete_ID=M.Athlete_ID
                        where M.Athlete_ID is null;"""
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"NumOfAthletesNotOnMedallists:{row[0]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==13:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="select Avg(Age) as Average_Age, Sport from Athlete Group By(Sport);"
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"AverageAge:{row[0]}, Sport: {row[1]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==14:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                sql="""select A.Athlete_Name as Athlete1, B.Athlete_Name as Athlete2, A.sport
                        from Athlete A, Athlete B
                        where A.sport=B.sport
                        AND A.Athlete_ID <> B.Athlete_ID
                        order by (A.sport); """
                mycursor.execute(sql)
                result=mycursor.fetchall() #fetch all the results
                for row in result:
                    print(f"Athlete1:{row[0]}, Athlete2: {row[1]}, Sport:{row[2]}")
                print(mycursor.rowcount, "rows.")
                input("Please enter key to continue ...")
                
            elif Choice==15:
                #when the user enter 15 for exit, the program will return to the main menu with a delay of 1 second for the user reaction time
                print("Returning to the main menu...")
                time.sleep(1) #pause the execution for 1 second

            else:
                #when user has enter a number that is not between 1 to 15 inclusive, it is considered as invalid input and user will have to re-enter
              print("Invalid input. Please enter again")
              print("Returning to the menu ...")
              time.sleep(1) #pause the execution for 1 second

    elif i==2: #Insert a new data
        Choice=0
        while Choice!=3: 
            #clearing the screen before printing the menu to the user
            os.system("clear")
            print("Which table do you want to insert data: ")
            print("1) Athlete")
            print("2) Coach")
            print("3) Exit")
            Choice=int(input("Your choice: ")) #receiving an int input from the user
            if Choice==1:
                #the following carries out the insert function into the database
                Athlete_ID=input("Please enter the AthleteID and do not enter anything between 400-798: ")
                Athlete_Name=input("Please enter AthleteName: ")
                Gender=input("Please enter the athlete gender(F/M): ")
                Sport=input("Please enter the sport: ")
                #Athlete table requires the attributes of Coach_name and Coach_ID which will be displayed to the users for selection after a sport is entered.
                sql="select Coach_Name, Coach_Id, Sport from Coach where Sport=%s"
                Val=(Sport,) #pass the parameter as a tuple
                mycursor.execute(sql, Val)
                result=mycursor.fetchall()
                print("Here're the coach in charge of " + Sport)
                for row in result:
                    print(f"Coach Name:{row[0]}, Coach ID: {row[1]}")
                print("Please select the Coach Name and ID based on details above when asking for the coach details.")
                Competition_Type=input("Please enter the competition_Type(Individual/Team): ")
                Coach_Name=input("Please enter the coach name: ")
                Country=input("Please enter the short country name represented by the athlete: ")
                Team_Name=input("Please enter the team name, enter null is the athlete has no team: ")
                Coach_ID=input("Please enter the coachID and enter any number between 1 to 300: ")
                Age=input("Please enter the age of the athlete: ")
                InsertQuery="""Insert into Athlete(Athlete_ID,Athlete_Name,Gender,Sport,Competition_Type,Coach_Name,Country,Team_Name,Coach_ID,Age) 
                Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                Values=(Athlete_ID,Athlete_Name,Gender,Sport,Competition_Type,Coach_Name,Country,Team_Name,Coach_ID,Age)
                mycursor.execute(InsertQuery,Values)
                mydb.commit() #commit the changes after execution
                print(mycursor.rowcount, "record inserted")
                input("Press enter key to continue ...")
                
            elif Choice==2:
                 #the following code carries out the same function as the code above but different sql query, please refer to the above comments if require
                Coach_ID=input("Please enter the coachID and do not enter any number between 1 to 300: ")
                Coach_Name=input("Please enter the coach name: ")
                Gender=input("Please enter the coach gender(F/M): ")
                Country=input("Please enter the country where the coach belongs to: ")
                Sport=input("Please enter the sport coached by the coach: ")
                InsertQuery="""Insert into Coach(Coach_ID,Coach_Name,Gender,Country,Sport)
                Values(%s,%s,%s,%s,%s)"""
                Values=(Coach_ID,Coach_Name,Gender,Country,Sport)
                mycursor.execute(InsertQuery, Values)
                mydb.commit()
                print(mycursor.rowcount, "record inserted")
                input("Press enter key to continue ...")
            
            elif Choice==3:
                print("Returning to the main menu ...")
                time.sleep(1)
                
            else:
                print("Invalid input. Please enter again.")
                
    elif i == 3:  #Update a new data
        Choice=1
        while Choice !=2:
            os.system("clear")
            print("Which table do you want to update: ")
            print("1)Athlete")
            print("2)Exit")
            Choice = int(input("Your choice: "))
            if Choice == 1:
                new_name = input("Please enter the new name of the athlete: ")
                athlete_id = input("Please enter the athlete id that you want to update: ")
                sql="CALL UpdateAthleteName(%s,%s,@UpdatedName)" #calling th stored procedure created previously
                Val=(new_name,athlete_id)
                mycursor.execute(sql,Val)
                mydb.commit() #commit the changes
                mycursor.execute("SELECT @UpdatedName")
                result=mycursor.fetchone()
                print(f"The updated name is: {result}")
                print(mycursor.rowcount, "record(s) affected")
                input("Press enter key to continue ...")
            
            elif Choice==2:
                print("Returning to the main menu...")
                time.sleep(1)
                
            else:
                print("Invalid input. Please enter again")
                time.sleep(1) 
    
    elif i==4: #Delete data
        Choice=1
        while Choice!=3:
            os.system("clear")
            print("Which table do you want to delete data from ")
            print("1)Athlete")
            print("2)Event")
            print("3)Exit")
            Choice=int(input("Your choice: "))
            if Choice==1:
                AthleteID=input("Please enter the athlete id that you want to delete: ")
                sql="CALL DeleteAthleteName(%s, @DeletedName)"
                Val=(AthleteID,)
                mycursor.execute(sql,Val)
                mydb.commit()
                mycursor.execute("SELECT @DeletedName;")
                result=mycursor.fetchone()
                print(f"The deleted name is: {result}")
                print(mycursor.rowcount, "record(s) affected")
                input("Press enter key to continue ...")
            
            elif Choice==2:
                DeletedSport=input("Please enter the sport that you want to delete: ")
                print("Since there are athlete who has already register for the sport, you have to enter the sport that you want to replace with.")
                ReplacedSport=input("Please enter the sport that you want to replace with: ")
                sql="call DeleteAndReplaceSports(%s,%s)"
                Val=(ReplacedSport,DeletedSport)
                mycursor.execute(sql,Val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
                input("Press enter key to continue")
                
            elif Choice==3:
                print("Returning to the main menu ...")
                time.sleep(1)
                    
            else:
                print("Invalid input. Please enter again.")
                time.sleep(1)
            
    elif i==5:
        print("Thank you for using the program. Bye!!")
    
    else:
        print("Invalid input. Please enter again.")
                    
mycursor.close()
mydb.close()
        

