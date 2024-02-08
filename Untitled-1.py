print("\n\tFuel Conversion: Gallon -> litre, mile -> kilometre, and vice versa")
def litre_100km_to_mile_gallon(litre):
    gallon=litre / 3.785
    mile= 100*1000/1609.34
    return mile/gallon
def mile_gallon_to_litre_100km(mile):
    litre_per_gallon=3.785 
    kilometer= 1609/1000
    return 100 / ((mile * kilometer)/ litre_per_gallon)
print("""Select the following conversions:
1. Mile per gallon
2. 100 km per liter """)
option= int(input("\n"))
if option==1:
    litre=float(input("Enter quantity of fuel in litres: "))
    return_res= litre_100km_to_mile_gallon(litre)
    print(return_res,"\n")
elif option==2:
    gall=float(input("Enter quantity of fuel in gallons: "))
    return_res= mile_gallon_to_litre_100km(gall)
    print(return_res,"\n")
else:
    print("Invalid option!!")

def even_num_lst(ran): # function for giving out eve numbers
    lst = [] # a list in which even numbers will be put
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11)) #11 is the value of the parameter "ran"

def list_updater(lst): #funnction for giving squares of numbers in a range
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5] 
print(list_updater(foo)) #the variable 'foo' is initialized to be equal to the parameter "lst"



