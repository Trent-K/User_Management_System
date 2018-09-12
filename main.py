#USER MANAGEMENT SYSTEM
#######################
#System architecture to create, edit, and manage a userbase.
#Will handle all user identity management within
#Should be  built with easy future integration to other programs


#######################
###-Last Edit: 05/19/18
#######################
## EDIT NOTES
###################
##--Need to finish:
    ##Isnt there a list.find() method to get rid of the scanning used in my code?
    ##'Delete User' functionality needs to be finished
        ##Deleting is done by just removing from list...
        ##name matching/functionality not finished
        ##SKIPPED --> Need to give user an option to delete all matches
            ## --> Difficult to modify a list while going through a loop
        ##SKIPPED --> need to allow for names to be searched with tre* **** etc
    ##'show user by name' needs to work for two of the same names
        ##also work for dates - return both!
        ##also should work with just a first/last name
    ##need to control and catch name formats
    ##alot of 'for user in userslist' loops. maybe create scan(identifier) funct
    ##clean up code to be more top down (make functions where needed)
    ##Better way to 'showusers' ??
    #-------------------------------- Cool Additions
    ##cool GUI shit?
    ##Linked List cool GUI shit???


#imports
import sys
import user_class
import functions

#load users from csv file
functions.loadDatabase()


######################################### CORE PROGRAM - MAIN CONTROL FLOW
#-------------------------------------------------------------------------


while( True ):

    s=functions.display_home_message()

    print("**The value chosen is: ",s)
    if(s == "1"):
        user_class.User.showUsers()    
    elif(s == "2"):
        user_class.User.addUser()
    elif(s == "3"):
        functions.deleteUser()  
    elif(s == "4"):    
        print("'Show a User' selected")
        user_class.User.showUserByNameDate(input("Please enter a name or date identifier: "))
    elif(s == "5"):
        functions.save_database()      
    elif(s == "6"):
        print("\n\nYou have selected more option.\nThere are none at the moment \n;)\n")
    elif(s == "7"):
        print("Quitting Program....")
        #determine if should save or not then exit
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n\n")












#-------------------------------------------------------------------------
#---------------------------- JUNK CODE ----------------------------------


###creating initial users
##print("\n")
##user1 = user_class.User("Bob Micheals", functions.getUniqueNumber(), "12/11/87")
##user2 = user_class.User("Tom Smith", functions.getUniqueNumber(), "01/28/98")
##user3 = user_class.User("Sarah Smith", functions.getUniqueNumber(), "11/15/00")
##user4 = user_class.User("Sean Smith", functions.getUniqueNumber(), "07/14/89")
##user5 = user_class.User("tara toga", functions.getUniqueNumber(), "03/22/93")
##user2 = user_class.User("Tom Smith", functions.getUniqueNumber(), "11/12/92")
##user5 = user_class.User("tammy toga", functions.getUniqueNumber(), "03/22/83")
##user5 = user_class.User("trent Kierstead", functions.getUniqueNumber(), "12/10/87")




##print("\ntesting 'showname' function.....")
##index = 0 #this is the position in the Users list (first)
##User.showName(index)
##print("\ntesting 'showUserByPosition' function.....")
##index = 1 #this is the position in the Users list (first)
##User.showUserByPosition(index)
##User.showUsers()
