#Problem 2

#Program that tells you if you have a particular food on the menu
Menu=["Pasta","Bolognese","Pesto","Pea soup","Smoked salmon","Mushroom Pide","Green Curry","Fried tafu"]
Order=input('\033[94m'+"What is you order ?"+'\033[0m')
if Order in Menu:
    print('\033[1m','\033[93m'+"Yes!"+'\033[0m'+'\033[36m'+"We serve that"+'\033[0m')
else:
    print('\033[91m'+"We dont serve it"+'\033[0m')