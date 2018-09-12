#here have set up bare bones 'User' class for testing


import random
import bpy

class User:

    requirePassword = True
    maxUsers = 1000 #not used
    usersList = []

    def __init__(self, name, id_num, DOB):
        self.name = name
        self.id_num = id_num
        self.DOB = DOB
##        self.pointer = User.usersList(find(self, User.usersList) - 1) #how to point to previous user?
        self.usersList.append(self)

    def showUserByPosition(position):
        print(User.usersList[position].name)
        print(User.usersList[position].id_num)
        print(User.usersList[position].DOB,"\n")


    def showUsers():
        #shows each all user objects
        #could just use specific 'showUser' function for each
        print("\nThere are currently", len(User.usersList), "users in the system....")
        for user in User.usersList:
##            print("\n")
            print(user.name)
            print(user.id_num)
            print(user.DOB,"\n")


    def checkId_num(newNumber):
        for k in range(0,len(User.usersList)):
##            print("iteration # ", k, " = ", User.usersList[k].id_num)
            if(User.usersList[k].id_num == newNumber ):
                return False
        return True


def getUniqueNumber():
#check that there is not already this id_num in database 
    unique = False 
    while(not unique): 
        num = random.randrange(1,User.maxUsers)
        #print("Inside getUniqueNumber(), the number generated is: ",num)     
        if(User.checkId_num(num) == True):
            unique = True   
    return num


print("\n")
user1 = User("Bob Micheals", getUniqueNumber(), "12/10/87")
user2 = User("Tom Smith", getUniqueNumber(), "01/28/98")
user3 = User("Sarah Smith", getUniqueNumber(), "11/15/00")
user4 = User("Sean Smith", getUniqueNumber(), "07/14/89")
user5 = User("tara toga", getUniqueNumber(), "03/22/93")


print("\ntesting 'showUserByPosition' function.....")
index = 1 #this is the position in the Users list (first)
User.showUserByPosition(index)


print("\ntesting 'showUsers' function.....")
User.showUsers()


##################################################################


##https://stackoverflow.com/questions/26628525/importerror-no-module-named-bpy
#   NO MODULE NAMED BPI ERROR!!!!!!!!
import bpy

# deselect all
bpy.ops.object.select_all(action='DESELECT')

# selection
bpy.data.objects['user4'].select = True

# remove it
bpy.ops.object.delete()



print("\ntesting 'showUsers' after removing.....")
User.showUsers()
