# These are my practises of files variables,lists,conditionalstatements

name=input("enter your name")
age=input("enter your age")
print("My name is " +name+ "and my age is " +age)

firstname=["Joel","Vivin","Jess"]
secondname=["joy","aaron"]
lastname=["Sequeira","Dsouza","Maschernas","melvika"]

firstname[2]="Ruvel"
firstname.insert(2,"Jason")
secondname.pop(0)
secondname.append("drake")
secondname.append("Jose")
secondname.append("Mel")
secondname[1]="Raj"
lastname.pop(3)
lastname.insert(3,"Dcruz")

amountofelements=len(lastname)
print(amountofelements)

print(firstname)
print(secondname)
print(lastname)


Choose=input("Have you opted for football? Y/N ") #Choose,Access,Search
Footballplayers=["Messi","Dybala","Ronaldo","Martinez","Ramos","MBappe"]
Cricketplayers=["Dhoni","Rahul","Bumra","Jadeja","Kohli"]
MMAplayers=["MCGregor","Kabib","Tate","Samantha"]
if Choose=="Y":
    Access=input("Whats your name?")
    #Footballplayers=["Messi","Dybala","Ronaldo","Martinez","Ramos","MBappe"]
    if Access in Footballplayers:
        print("Good! your name is found in our list") #exits
    elif Access not in Footballplayers:
        print("You Sure You Are In Football?")
        Search=input("Reenter your name: ")
        if Search in Cricketplayers:
            print("You are in Cricket team,Fetching You back to menu..") #menu
        elif Search in MMAplayers:
            print("You are in MMA team,Fetching you back to menu..")  #menu
        else:
            print("Sorry you are not registered yet") #menu
else:
    print("thank you for visiting!")
    