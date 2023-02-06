#String formatting
# %s is only for strings, %d is for decimals, %f is for float 

name=input("Name?")
age= int(input("Age?"))
mylist=[1,2,3]
print("%s is %d" % (name,age))
print("mylist is %s" % mylist)

#twisty ( you can make this as optional)
data=("John","Doe",53.44)
print("hello %s %s your balance is %.2f" % data)