#Thanks for reaching here. These problems are for Python beginners.
#Just ignore this page if want to have a peek @ the problems directly.

response = input("What problem number would you like to run? ")
file_name="Problem " +response+ ".py"

#Really dodgy way of running the code that you select
with open(file_name,"r") as rnf:
     exec(rnf.read())