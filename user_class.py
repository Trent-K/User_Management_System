#class of users
###############
    #users will have name (first,last,middle)
    #Will also have id numbers, password (for editing/storage; hash?)
    #will have DOB, Notes... Include Easy add of any other data
    #include general 'note' object attribute - hold general text, note, addy, whatever the system wants to store


#need to finish 'deleteuser'

#Imports
import functions
import random
import csv

class User:

    database = "UserDatabase.csv"
    requirePassword = True
    maxUsers = 1000 #not used
    usersList = []
    myData = []

    def __init__(self, name, id_num, DOB):
        self.name = name
        self.id_num = int(id_num)
        self.DOB = DOB
        self.usersList.append(self)
        #link/point to previous user?
        
    #show all user's attributes
    def showObjectProperties():
        print("\nCurrent Objects in class: ")
        print("-------------------------")
        for j in range(0,len(User.usersList)):
            print(User.usersList[j].name)
            print(User.usersList[j].id_num)
            print(User.usersList[j].DOB, "\n")

    #can modify this function to be used to find match in 'delete' by id
    def checkId_num(newNumber):
        for k in range(0,len(User.usersList)):
            if(User.usersList[k].id_num == newNumber ):
                return False
        return True

    #show all the users and their attributes
    #could just use specific 'showUser' function for each
    def showUsers():
        print("\nThere are currently", len(User.usersList), "users in the system....")
        for user in User.usersList:
            print("\n")
            print(user.name)
            print(user.id_num)
            print(user.DOB)

    #adds a user with entered attributes
    def addUser():

        
##        newUser = User(input("please enter a name: "),(
##                  functions.getUniqueNumber()), (
##                  str(input("Please enter a date of birth:"))) )


        #new version which includes a 'grabdate' function
        #grab date uses 'input()' but cleanses data
        #dates must b format "mm/dd/yy"
        newUser = User(input("please enter a name: "),(
                  functions.getUniqueNumber()), (
                  str(functions.grabDate())) )


        
        print("\nNew user added...\n")


    #loading user and saving user functions
    #pull from 'database' and store to list
    #store list to 'database' file.....
    #do i need 'myFile.close()' functionality?
    def loadUsers():
        print("\n\n\nLoading users from database file: ", User.database)
        print("\n\n")
        # print("\n\nLoading Data.....\n\n")
        myFile = open(User.database, 'r')        
        with myFile:
            data = list(csv.reader(myFile))
##            print("\n\nAdding the following users:")
##            print("Name    idnum     DOB")
            for entry in data:
##                print(entry[0], "",entry[1],"",entry[2])
                newuser = User(entry[0], entry[1], entry[2]) #<------ use this method
 
    def saveUsers():
        tosave = []
        for i in range(0, len(User.usersList)):
            data = [User.usersList[i].name,
                         User.usersList[i].id_num,
                         User.usersList[i].DOB ]
            tosave.append(data)
        print("\n\nData Converted.....\n\n")
        myFile = open(User.database, 'w', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(tosave)
        print("\nDatabase saved....\n")








    #breaks if first/last name less thatn 3 chars...
    #what happens if there is no space first or last??
    def nameCompare(selector, username):

        #confirm lower case
        selector = selector.lower()
        username = username.lower()

        #seperate first/last from selector
        sel = selector[0:selector.find(" ")]
        sel=sel.replace(" ","")
        ector = selector[selector.find(" ")+1:]
        ector=ector.replace(" ","")

        #match names
        

        #if exact match
        if( selector == username):
            return True

        #just first or last name...
        elif( (username.find( sel ) != -1) or (username.find( ector ) != -1) ):
            return True

        #first 3 letters of first or last name?
        elif( (username.find( sel[:3] ) != -1) or (username.find( ector[:3] ) != -1) ):
             return True 



####### ^^^^^^^^^^^^^^^ LEFT OFF HERE 













   






























   # pUSSY 





#second revision of 'deleteuser'
#added 'grabDate' function so dates will always be clean
#should i do this for names also? first last or first middle last only
#need to finish id_num testing
#need to include invalid character catching for matches delete
#test and use this new funct


#Need to combine following code into : User.findmatch(selector)
##for k in range(0,len(User.usersList)):
##    if(User.usersList[k].DOB == selector ):
#maybe a single for loop calling findmatch() each time, cleans code up
    def delUser(selector):
   
        matches=[]

        #names/dates/ids are given raw from user
        #could put in anything '2311 trent'
            #if this happens there will simply be no match and continue

        #-id number or date
        if(functions.num_there(selector) ):
            print("\nNumber Found!!\nID Number or Date....\n\n")

            #if date in right format - if not exit
            if( (len(selector) == 8) and (selector[2] == "/") ):
                print("\n\n*Date identifier entered")

                for k in range(0,len(User.usersList)):
                    if(User.usersList[k].DOB == selector ):
                        #found date match
                        print("DOB match found at item # ", k)
                        matches.append(k)

            #for id number
            #doesssssnt work. gets to "Do Nothing"
            #number found in string, not in date format..
            #just scanning for a match works, if no match/id format then ok
##            elif( selector == id_num ):
            else:
            
                print("\nID Number entered.....")
                # print("\n\nSelector = ",selector)
                for k in range(0,len(User.usersList)):
                    # print("\n\nUser.usersList[k].id_num = ",User.usersList[k].id_num)
                    if( str(User.usersList[k].id_num) == selector ):
                        #found ID Number match
                        print("ID Number match found at item # ", k)
                        matches.append(k)
        #-name
        #----------------- Seems to work fine
        else:
            print("No Number!!\nname identifier")
            for k in range(0,len(User.usersList)):
                if( User.nameCompare( selector, User.usersList[k].name ) ): #returns true if direct match or close match
                    matches.append(k)


#-all matches gathered to array
#-now determine which to delete
#-should use:
        if( len(matches) == 1 ):
            #only one match...
            #present options to delete this one y/n
            print("\nOne possible match found\n")
            print("\nMatch Name: \n",User.usersList[matches[0]].name,"\n")
            toRemove=input("\nWould you like to delete a user? [Y/N]\n")
            
                                    #catch non integer input
            try:
               val = int(toRemove) #make sure its an integer
            except ValueError:     
               #not an int entered
                print("\n\nPlease enter a valid integer user index to delete...")
                return

            if( toRemove.lower() == "y" ):
                print("Deleting User")
                User.usersList.remove(User.usersList[ matches[0] ])
                #breaks for multiple same names? (wouldnt be in this block then right>
                #is there a better way to delete?
                    #usersList.remove( index )??
            else:
                print("\nContinuing without deletion....")
            
        elif( len(matches) > 1):
            #multiple matches
            #present options for multiple matches..
            print("\n\n\nMultiple matches found!\n\nPrinting matches:")
            for match in matches:
                print(User.usersList[match].name)
            toRemove = input("""\n\nWould you like to delete a user?
                             If yes, enter which user
                             ----------------------
                             1 - First Match Shown
                             2 - Second Match Shown
                             n - nth match....\n""")

#NEED TO CLEANSE INPUT HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #breaks when pressing <Enter>

                                    #catch non integer input
            try:
               val = int(toRemove) #make sure its an integer
            except ValueError:     
               #not an int entered
                print("\n\nPlease enter a valid integer user index to delete...")
                return
            
            print("\nYou have selected item number",toRemove,"to remove\n") 
            print("\nDeleting user number",toRemove,"with name",selector,"\n")
            print("This will delete user #",matches[int(toRemove)-1],"from master list")
            User.usersList.remove(User.usersList[matches[int(toRemove)-1]]) #the second match will really be @ index n-1 in array
            print("\nUser Deleted....\n")

        #no matches
        #can really delete this code below..
        else:
            print("\nDo Nothing...")


#######################################























    #delete a user by different identifiers
    #enter in name, id, or DOB. Code determines which
    #------------------------------------------------
    #Deleting Functionality Working
        #- Name deletion works for exact match, first/last name match ~works
        #--- Just removed from array, object still exists
        #--- Was a weird error from deleting by id but seems to be fixed
        #--- Could include better error handling here   
    #All the if/else conditionals work to select for name/id/date
    #list of multiple first name or last name close matches is presented, but can only del one at a time
    def deleteUser(selector):
        matches=[]
  
        if(functions.num_there(selector)):
           #either id number or date
           #works for exactly matched id numbers
           print("\n\n*Number identified in the selector\n")
           if( (len(selector) > 2) and (selector[2] == "/") ):
               # DATE
               #control for dates entered incorectly: "1/1/94, 12/3/89"
               print("\n\n*Date identifier entered")
               if(len(selector) == 8):
                   #scan objects for date match.....
                   print("Correct Date Format entered")
                   #match dates
                   for k in range(0,len(User.usersList)):
                       if(User.usersList[k].DOB == selector ):
                           #found date match
                           print("DOB match found at item # ", k)
                           print("Deleting user with DOB: ", selector)
                           User.usersList.remove(User.usersList[k])
               else:
                   #include code to check if "/" is in the string somewhere? 9/12 chance this error could happen 4/13/21, etc
                   print("Incorrect Date Format....")
                   
                   
           else:
               print("\n*ID Number identifier entered")
               #match id numbers
               for k in range(0,len(User.usersList)):
                   if(User.usersList[k].id_num == int(selector) ):
                       #found id number match
                       print("ID Number match found at item # ", k)
                       print("Deleting user with id number: ", selector)
                       User.usersList.remove( User.usersList[k] )
                       return
               print("\n\nNo matching ID number found in database.....\n\nReturning to program....\n")



        else:
            # NAME - there are no numbers
            # for exactly matched names - if two by same name then gives option to delete either
            print("\n\nName identifier entered")
            selector=selector.lower()
            #search for direct match
            for k in range(0,len(User.usersList)):
                if(User.usersList[k].name.lower() == selector ):
                    print("\nExact name match found!\nMatch at index: ",k)
                    matches.append(k) # to allow for multiple matches 
            
            if( len(matches) > 0):
                #show one or more matches
                #need to add more info on entries name1 = name2....
                print("\n\n\nPerfect matches found!\n\nPrinting matches:")
                for match in matches:
                    print(User.usersList[match].name)
                toRemove = input("""\n\nWould you like to delete a user?
                                 If yes, enter which user
                                 ----------------------
                                 1 - First Match Shown
                                 2 - Second Match Shown
                                 n - nth match....\n""")
                print("\nYou have selected item number",toRemove,"to remove\n") 
                print("\nDeleting user number",toRemove,"with name",selector,"\n")
                print("This will delete user #",matches[int(toRemove)-1],"from master list")
                User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ]) #the second match will really be @ index n-1 in array
                print("\nUser Deleted....\n")
                
            else:
                #no exact matches found yet!
                print("\nNo perfect name match found!")
                
                #search for just first name or last name
                #there is a space in the name entered (first and last entered)
                if(selector.find(" ") != -1):
                    
                    print("\nFirst and last name entered..")
                    #get the first name and last name
                    sel = selector[0:selector.find(" ")]
                    ector = selector[selector.find(" ")+1:]
                    print("""\nNo user found with exact name match.
                          Selector entered with a first and last name.""")
                    print("After splitting the selector, \nsel = ",sel,"\nector = ",ector,"\n")
                    print("------------------------------------------------$$")
                    #checking for first/last name matches only...
                    print("\nChecking the list of users for possible matches..")
                    for k in range(0,len(User.usersList)):                   
                        #print("\nChecking for the same first/last names..")
                        first = User.usersList[k].name[0:User.usersList[k].name.find(" ")]
                        last = User.usersList[k].name[User.usersList[k].name.find(" "):]
                        first = first.replace(" ","").lower() #strips any spaces
                        last = last.replace(" ","").lower()
##                        print("\nFirst name is: \n",first)
##                        print("\nLast name is: \n",last)

                        #check if first names match, or last name....
                        if( first == sel):
##                            print("First name match @ k = ",k)
##                            print("Selector entered: ", selector)
##                            print("Matched User: ",User.usersList[k].name)
####                            print("User with same first name found: /nUser: ",User.usersList[k].name,"\n user id: ",User.usersList[k].id_num,"\n\n"))
                            matches.append(k)
                        elif(last == ector):
##                            print("\n\nLast name match @ k = ",k)
##                            print("Selector entered: ", selector)
##                            print("Matched User: ",User.usersList[k].name)
####                            print("User with same last name found: /nUser: ",User.usersList[k].name,"\n user id: ",User.usersList[k].id_num,"\n\n"))
                            matches.append(k)


############                        #need to replace alot of the code above with 
############                        elif( selector.find(User.usersList[k].name) == User.usersList[k].name ):
############################## THIS CODE NEEDS TO BE REDONE....
############################# ------ ALSO USE .find( first_three_letters_of_first) and  .find( first_three_letters_of_last)                          



                    ##Code works as intended
                    #--------------- CAN ONLY ALLOW FOR ONE DELETION AT A TIME
                    if( len(matches) > 0):
                        print("\n\nNo direct matches, here are some similar results:\n")
                        for match in matches:
                            print(User.usersList[match].name)

                        #allow user to select from ~matches and delete....
                        toRemove = input("""\nWould you like to delete a user?
                                         If yes, enter which user
                                         ----------------------
                                          0 - Delete No Matches
                                          1 - First Match Shown
                                          2 - Second Match Shown
                                          n - nth match....\n""")

                        #catch non integer input
                        try:
                           val = int(toRemove) #make sure its an integer
                        except ValueError:     
                           #not an int entered
                            print("\n\nPlease enter a valid integer user index to delete...")
                            return

                        #make sure integer that is entered is within valid ranges
                        if( int(toRemove)-1 < len(matches) and (matches[int(toRemove)-1] < len(User.usersList)) ):
                            print("\n\nDeleting User: ",User.usersList[int(toRemove)]) #make sure its in range
                        else:
                            print("\n\n\nNumber outside range.\nExiting....\n\n\n")
                            return

                        #for debugging
##                        print("\n\nYou have selected: ",toRemove)
##                        print("The 'matches' entry assocuated with to remove is: \n int(toRemove) - 1 = ", int(toRemove) - 1)
##                        print("matches = ",matches)
##                        print("len(User.usersList) = ",len(User.usersList))
                        
                        if( toRemove == "0" ):
                            print("\nDeleting no matches and continuing..\n\n")   
                        else:
                            User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ])
                            print("\n\nUserDeleted...\n\n")
                        

                    #if there is no space in the selector/identifier
                    #just one word, so look at first/last name
                    else:
                        print("\nNo near matches found...")
                else:
                    print("\nPlease enter a first and last name\n\n")

 

            












    #shows a specific user based on position in the list
    #enter an integer, used as the position
    #will show that specific user's properties
    def showUserByPosition(position):
        print(User.usersList[position].name)
        print(User.usersList[position].id_num)
        print(User.usersList[position].DOB,"\n")


    #user display, only takes name or date as identifier [STRING]..
    #---- need to include error handling for no match!!!!!!!
    #works - need to handle errors (multiple names/dates)
    #needs to work how 'delete' works (can enter name, date, dob)
    def showUserByNameDate(identifier):    
        if( type(identifier) == str):
            print("String identifier")
            print("Please enter a name or date:")
            if( (len(identifier) > 3) and (identifier[2] == '/')):
                print("Date identifier")
                for j in range(0,len(User.usersList)):
                    if( User.usersList[j].DOB == identifier):
                        print("\nDate match found!!")
                        User.showUserByPosition(j) #this is better version
                        return
                print("\nNo match found....")
                        
            else:
                print("Name identifier")
                #need to match and present
                for j in range(0,len(User.usersList)):
                    #find index with that name
                    if( User.usersList[j].name.lower() == identifier.lower()):
                        print("\nName match found!!")
                        User.showUserByPosition(j)
                        return
                print("\nNo match found....")
                
        
    def showUserPosition(self):
        #not done
        return True
    def showName(identifier):
        print(User.usersList[identifier].name)
        
#-------------------------------------------------------------------------
#---------------------------- GENERAL FUNCTIONS --------------------------


#------------------------------moved
##def getUniqueNumber():
###check that there is not already this id_num in database 
##    unique = False 
##    while(not unique): 
##        num = random.randrange(1,User.maxUsers)
##        #print("Inside getUniqueNumber(), the number generated is: ",num)     
##        if(User.checkId_num(num) == True):
##            unique = True   
##    return num
##
##def deleteUser():
##    print("\nDeleting user...")
##    selector = input("Please enter a name, ID number, or date: ")
##    User.deleteUser(selector)
##        
##def num_there(s):
##    return any(i.isdigit() for i in s)
##
##
###save database to csv file
##def save_database():
##    
##    print("\nSaving Database....\n")
##    file_target = ""
##    
##    return 1

#-------------------------------------------------------------------------
#---------------------------- TESTING ------------------------------------

######----------------------------MOVED TO main.py
######print("\n")
######user1 = User("Bob Micheals", getUniqueNumber(), "12/11/87")
######user2 = User("Tom Smith", getUniqueNumber(), "01/28/98")
######user3 = User("Sarah Smith", getUniqueNumber(), "11/15/00")
######user4 = User("Sean Smith", getUniqueNumber(), "07/14/89")
######user5 = User("tara toga", getUniqueNumber(), "03/22/93")
######user2 = User("Tom Smith", getUniqueNumber(), "11/12/92")
######user5 = User("tammy toga", getUniqueNumber(), "03/22/83")
######user5 = User("trent Kierstead", getUniqueNumber(), "12/10/87")
######
######
######
########print("\ntesting 'showname' function.....")
########index = 0 #this is the position in the Users list (first)
########User.showName(index)
########print("\ntesting 'showUserByPosition' function.....")
########index = 1 #this is the position in the Users list (first)
########User.showUserByPosition(index)
########User.showUsers()
######
######
################################################################### ACTUAL PROGRAM - MAIN CONTROL FLOW
#######-----------------------------------------------------------------------------------------------
######
######while( True ):
######
######    #need to include save option.....
######    print("\nHello! Welcome to the user management system")
######    s = input("""Would you like to __
######          1 - See Current Users
######          2 - Add User
######          3 - Delete User
######          4 - Show a User
######          5 - Save Database
######          6 - More Options
######          7 - Quit\n""")
######
######    print("**The value chosen is: ",s)
######    if(s == "1"):
######        User.showUsers()    
######    elif(s == "2"):
######        User.addUser()
######    elif(s == "3"):
######        deleteUser()  
######    elif(s == "4"):    
######        print("'Show a User' selected")
######        User.showUserByNameDate(input("Please enter a name or date identifier: "))
######    elif(s == "5"):
######        save_database()
######    elif(s == "6"):
######        print("\n\nYou have selected more option.\nThere are none at the moment \n;)\n")
######    elif(s == "7"):
######        print("Quitting Program....")
######        #save database
######        #User.backup()
######        sys.exit(0)
######    else:
######        print("Please enter a valid key...")
######    print("\n\n")
          
    
################################################ Cool Graphic Display Idea

#also want spherical, nodal relationship....
    #With graphical display (layered with different radii r = 1,2...n)
    #should show a nodal relationship
        #center node at orgin branching out from there. Similar to:
            #https://www.gettyimages.com/detail/photo/an-isohedron-nodal-network-high-res-stock-photography/520760056
            #http://www.slingshotfilms.it/a-good-american/
    #what graphical display looks coolest?
        #each node connected to nearest nodes, or just connected to previous
    #linked list or just List

##########################################################################




############################################################# JUNK/ARCHIVE

##    def loadUsers():
##            for row in myFile:
##                print("Data type: ",type(row))
##                print(row[1]) #grabs the first letter of the row
##                print(reader.readrows()) 
##                #the entire row is taken in as a single string..
##                #need to split up into 3 data points
##                    #or find a way to grab cell by cell


##data=list(csv.reader(csvDataFile))
#need to finish building the loading user functionality here...







##User.showObjectProperties()
##
##
#####print properties
##print("--Show each object and attributes--")
##print(user1)
##print(user1.name)
##print(user1.id_num)
##print(user2)
##print(user2.name)
##print(user2.id_num)
##print(user3)
##print(user3.name)
##print(user3.id_num)
##
##
##print("\n--Show general values--")
##print(User.requirePassword)
##print(User.maxUsers)


#show list of each User created




        ##        #for position identifier              #NOT WORKING
##        if( type(identifier) == int):
##            print(User.usersList[identifier].name)
##            print(User.usersList[identifier].id_num)
##            print(User.usersList[identifier].DOB,"\n")





##    #delete a user by different identifiers
##    #should have class functions: deleteID, deleteName,
##    #have rest of function outside in other general functs
##    def deleteUser():
##        in2 = input("""Would you like to __
##                  1 - Delete User by ID Number
##                  2 - Delete User by name
##                  3 - Go Back\n""")
##        print("the value chosen is: ",in2)
##
##        if(in2 == "1"):
##            print("Deleting by ID Num")
##        elif(in2 == "2"):
##            print("Deleting by name")
##        elif(in2 == "3"):
##            print("Going Back")
##        else:
##            print("invalid key. Going back...")
##            #need to include better handling here
##



##        if(selector == "PLACEHOLDER"):          #THIS NEEDS TO SWITCH
##            #search/match name
##            #delete by name
##            #remove from list
##            print("Deleting by ID name...")
##        elif(selector == "Trent"):
##            #search/match id number
##            #delete by name
##            #remove from list
##            print("Deleting by ID Number...")
##            for k in range(0,len(User.usersList)):
##                if(User.usersList[k].id_num == int(selector) ):
##                    #found id number match
##                    print("ID Number match found at item # ", k)
##                    #   NO MODULE NAMED BPI ERROR!!!!!!!!
##        elif(selector[2] == "/"):
##            #search/match id number
##            #delete by name
##            #remove from list
##            print("Deleting by date identifier...")







################ __________________________ BATCH DELETION CODE _____________________________________________________________




##                        #catch non integer input
##                        try:
##                           val = int(toRemove)
##                        except ValueError:     
##                           #not an int entered
##                            if(toRemove.lower() == "a"):
##                                print("\n\nDeleting all matches\n")
##                                print("\n\nUsersList = \n",User.usersList)
##                                print("\nmatches = \n",matches)
####                                for xx in range(len(matches),0):
##                                for mtch in reversed(matches):
##                                    print( "index = ",mtch)
##                                    print("To be deleted: ", User.usersList[mtch])
##                                    del User.usersList[matches[mtch]]
##
###---------the array is getting smaller and the index becomes out of range...
##                                    
####################                                    print("\n",match)#these are ints
####################                                    print("\nUser.usersList[ match ] = ",User.usersList[ match ])
######################                                    User.usersList[match]
######################                                    User.usersList.remove( User.usersList[ match ] )
####################                                    User.usersList[match]
####################                                    User.usersList.remove( User.usersList[ match ] )
######################                                    User.usersList.remove( User.usersList[ matches[int(match) - 1] ])
######################                                    User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ])
##                                    
###------------------#delete all matches here...
##                                return
##                            else:
##                               print("\n\nInvalid Key Entered....\nReturning to main window...\n")
##                               return
##
##
##
##
##
##                        #for debugging
##                        print("\n\nYou have selected: ",toRemove)
##                        print("The 'matches' entry assocuated with to remove is: \n int(toRemove) - 1 = ", int(toRemove) - 1)
##                        print("matches = ",matches)
##                        print("len(User.usersList) = ",len(User.usersList))
##
##
##
###---------- NEED TO FINISH AND TEST THE NEXT FE CONDITIONAL STATEMENTS
##                        
##                        if( toRemove == "0" ):
##                            print("\nDeleting no matches and continuing..\n\n")   
##                        elif(matches[ int(toRemove) - 1] >= len(User.usersList) ):
##                            #delete nth match
##                            #the entered index is within the range of the list of users
##                            print("Entered number is inside range...\nDeleting entry....")
##
##
##
##                        
##
##                    #if there is no space in the selector/identifier
##                    #just one word, so look at first/last name
##                    #leaving this empty for now....
##                    else:
##                        print("\nNo matches found...")
##                else:
##                    print("\nPlease enter a first and last name\n\n")

        
        ##                        print("\nYou have selected item number",toRemove,"to remove\n") 
##                        print("\nDeleting user number",toRemove,"with name",selector,"\n")
####                        print("This will delete user #",matches[int(toRemove)-1],"from master list")
####                        User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ]) #the second match will really be @ index n-1 in array
##                        print("\nUser Deleted....\n")
#---------errors if you enter a number outside of range toremove = 10
#---------allow for batch deletion...
#---------allow an exit key (delete none)



#############
####            def saveUsers():
####
####        tosave = []
####        
######        print("\n\n\nBeing Built......\n\n")
######        print("\n\nSavings users to database file: ", User.database)
######        #need to build the saving user from csv here...
######        print("\nBefore adding anyhting,\nmyData = \n",User.myData)
######        print("\n\nThe size of userlist [ len(User.usersList) ] =",len(User.usersList))
######        print("\n")
####        
####
######        print("\nList of users:\n")
######        for x in range(0,len(User.usersList)):
######            print("user: ",User.usersList[x])
######            print("name = ",User.usersList[x].name)
######            print("id_num = ",User.usersList[x].id_num)
######            print("id_num = ",User.usersList[x].DOB)
######            print("\n")
######            
####
####        
####        for i in range(0, len(User.usersList)):
######            print("\n\n i = ",i,"\n\n") 
####            data = [User.usersList[i].name,
####                         User.usersList[i].id_num,
####                         User.usersList[i].DOB ]
####            tosave.append(data)
####        print("\n\nConverting data.....\n\n")
######        print("\nmyData = \n",tosave)
######        print("\n")
######        for d in tosave:
######            print("\n")
######            print(d)
####
#####data formatted
####        myFile = open(User.database, 'w', newline='')
####        with myFile:
####            writer = csv.writer(myFile)
####            writer.writerows(tosave)
####
