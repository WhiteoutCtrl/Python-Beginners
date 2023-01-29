#list of elements
names=["John","Jack"]
#adds element to the back of the list
names.append("Ethan")
#adds element to specified position
names.insert(0,"Jessica")
#removes and replaces element with given element & position
names[1]="Ruvel"
#pops the element of the list of specified position
names.pop(0)
print(names)

#other method to print names from list
secondname=names[1]
print(secondname)

#little creativeness
firstnames=['Johnson','Ruvel','Andrea']
midnames=['Joy','Elizabeth','Aaron']
surnames=['Dsouza','Mascarehnas','Sequeira']
A=firstnames[1]
B=midnames[2]
C=surnames[1]
print(A+" "+B+" "+C)

#to measure the length (the number of elements) of the list
#lets measure on list "surnames"
amountofnames=len(surnames)
print(amountofnames)   #remember elements start with address 0 & not 1.