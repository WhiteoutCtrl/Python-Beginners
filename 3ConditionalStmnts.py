# CONDITIONAL STATEMENTS ( Multiple statemnets to try , comment each block 1 by 1 and execute)

name="Rick"
age=10
if name == "John" and age == 10:
    print("Welcome John of age 10")

if name == "John" or name == "Rick":
    print("Welcome John and Rick")
print("1-----------------------------------------------------------------")

# CHANGING INDENTATION TRACK
name="Rick"   # <-- Try changing names here
if name == "John":
    print("Welcome John")

    if name == "Rick":   #this wont give O/P
        print("Welcome Rick") #Until the 1st condition sets TRUE it wont jump to 2nd
print("2-----------------------------------------------------------------")

# MAKE IT EAZZY
name="Jason" # < -- Try changing names here
GroupA = ["John","Joe","Rick"]
GroupB = ["Ruvel","Vivin","Lionel"]
if name in GroupA:
    print("Bonjour Group A")
if name in GroupB:
    print("Bonjour Group B")
print("3-----------------------------------------------------------------")

# EXTRA SPICE
name="Andrea"
GroupA = ["John","Joe","Rick"]
GroupB = ["Ruvel","Vivin","Lionel"]
if name in GroupA:
    print("Bonjour Group A")
if name in GroupB:
    print("Bonjour Group B")
elif name == "Andrea":
    print("Will soon be assigned to groups")
else:
    print("Not in list, Check the registrar")
print("4-----------------------------------------------------------------")

# ADDITIONAL "IS" AND "NOT" OPERATORS
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(y is x) #IS operator returns TRUE if variables are same, returns FALSE if variables are different
print("***************")
print(2 is not 2)
print(2 is 2)   #NOT operator inverts result,returns TRUE if FALSE & FALSE if TRUE
print(not False)
print(not True)
