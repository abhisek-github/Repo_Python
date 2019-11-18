"""
#3 python tutorial

print(r'C:\ABHISEK\na')
#4 python Variables

v_str = "Youtube"
print(v_str[1:4])
print(v_str)
"""
#5 List in python
"""
v_l1 = [24,56,76,43,67]
print(v_l1[2])
print(v_l1[-3])
v_l2 = ["Abhi","sai","mani","naveen"]
print(v_l2)
v_l_m = [v_l1,v_l2]
print(v_l_m)
"""
#Ex - 2
"""
v_list1 = ["Abhi","Xty","jgh","jdj","hfhf"]
print(v_list1)
print(v_list1[1].title())
v_bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(v_bicycles[5]) #IndexError: list index out of range
print(v_bicycles[-1])
#print(v_bicycles[-6]) #IndexError: list index out of range
v_msg_var = "My first bicycle was" +" "+ v_bicycles[0] + "."
print(v_msg_var)
"""
#Changing ,adding,removing elements in list
"""
v_motorcycles = ['honda', 'yamaha', 'suzuki']
print(v_motorcycles)    #   ['honda', 'yamaha', 'suzuki']
# Changing
v_motorcycles[0] = "Ducati"
print(v_motorcycles)    #   ['Ducati', 'yamaha', 'suzuki']
# Adding
v_motorcycles.append('hero')
print(v_motorcycles)    #   ['Ducati', 'yamaha', 'suzuki', 'hero']
v_motorcycles.insert(2,'Bajaz')
print(v_motorcycles)    #   ['Ducati', 'yamaha', 'Bajaz', 'suzuki', 'hero']
# Removing
del v_motorcycles[2]
print(v_motorcycles)    #   ['Ducati', 'yamaha', 'suzuki', 'hero']
# pop()
v_popped = v_motorcycles.pop()
print(v_popped) #   hero [here we will get the popped item]
print(v_motorcycles)    #   ['Ducati', 'yamaha', 'suzuki']
print("The last bike I owned was a"+" "+v_popped.title()+".")
v_popped = v_motorcycles.pop(1)
print(v_motorcycles)    #   ['Ducati', 'suzuki']
# remove()
v_rem = "Ducati"
v_motorcycles.remove(v_rem)
print(v_motorcycles)
print("\nA"+" "+v_rem+" "+"is too expensive for me.")
"""
# Practice Task from Book
# Q1. [If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner. ]
"""
v_guest_list = ["Adam","Scott","Allen","Miller","Jhon"]
for guest in v_guest_list :
    print("Welcome Mr."+guest+" "+"to my beautiful villa.")
"""
#output
"""
Welcome Mr.Adam to my beautiful villa.
Welcome Mr.Scott to my beautiful villa.
Welcome Mr.Allen to my beautiful villa.
Welcome Mr.Miller to my beautiful villa.
Welcome Mr.Jhon to my beautiful villa.
"""
# Q2.[Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.]
"""
v_guest_list = ["Adam","Scott","Allen","Miller","Jhon"]
#for guest in v_guest_list :
#    print("Welcome Mr."+guest+" "+"to my villa.")
v_guest_list[1] = "Abhi"
v_guest_list[2] = "Likun"
#print(v_guest_list)
for update_guest in v_guest_list :
    print("Sorry for your inconvenience Mr."+update_guest+","+"\n"+"\tPlease make yourself comfortable.")
"""
# Output
"""
Sorry for your inconvenience Mr.Adam,
	Please make yourself comfortable.
Sorry for your inconvenience Mr.Abhi,
	Please make yourself comfortable.
Sorry for your inconvenience Mr.Likun,
	Please make yourself comfortable.
Sorry for your inconvenience Mr.Miller,
	Please make yourself comfortable.
Sorry for your inconvenience Mr.Jhon,
	Please make yourself comfortable.
"""
#Q3.[More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.Use insert(),append()]
"""
v_guest_list = ["Adam","Scott","Allen","Miller","Jhon"]
#for guest in v_guest_list :
#    print("Welcome Mr."+guest+" "+"to my villa.")
v_guest_list[1] = "Abhi"
v_guest_list[2] = "Likun"
#print(v_guest_list)
#for update_guest in v_guest_list :
#    print("Sorry for your inconvenience Mr."+update_guest+","+"\n"+"\tPlease make yourself comfortable.")
v_guest_list.insert(1,"Sai")
v_guest_list.append("Gudu")
v_guest_list.append("Sourav")
#print(v_guest_list)
for update_guest_add in v_guest_list :
    print("Hello Mr."+update_guest_add+","+"\n"+"\t Welcome.")
"""
# Output
"""
Hello Mr.Adam,
	 Welcome.
Hello Mr.Sai,
	 Welcome.
Hello Mr.Abhi,
	 Welcome.
Hello Mr.Likun,
	 Welcome.
Hello Mr.Miller,
	 Welcome.
Hello Mr.Jhon,
	 Welcome.
Hello Mr.Gudu,
	 Welcome.
Hello Mr.Sourav,
	 Welcome.
"""
#Q.4 [You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.]
"""
v_guest_list = ["Adam","Scott","Allen","Miller","Jhon"]
#for guest in v_guest_list :
#    print("Welcome Mr."+guest+" "+"to my villa.")
v_guest_list[1] = "Abhi"
v_guest_list[2] = "Likun"
#print(v_guest_list)
#for update_guest in v_guest_list :
#    print("Sorry for your inconvenience Mr."+update_guest+","+"\n"+"\tPlease make yourself comfortable.")
v_guest_list.insert(1,"Sai")
v_guest_list.append("Gudu")
v_guest_list.append("Sourav")
del v_guest_list[3:]
print(v_guest_list)

for update_guest_add in v_guest_list :
    print("Hello Mr."+update_guest_add+","+"\n"+"\t Welcome.")
"""
# Organizing a List.
# sorting a list using sort() method:
"""
v_guest_list = ["Adam","Blake","Scott","Allen","Miller","Jhon"]
v_guest_list.sort()
print(v_guest_list)
v_guest_list.sort(reverse=True)
print(v_guest_list)
v_guest_list.sort(reverse=False)
print(v_guest_list)
"""
# Example
"""
v_guest_list = ["Lucky","Adam","Blake","Scott","Allen","Miller","Jhon"]
print("\nHere is the original list")
print(v_guest_list)
print("\nHere is the sorted list")
print(sorted(v_guest_list))
print("\nHere is original after sorted function")
print(v_guest_list)
v_cars = ['Bmw', 'audi', 'Toyota', "chai","bmw",'subaru']
print(v_cars)
v_cars.sort()
print(v_cars)
print(sorted(v_cars))
"""

# Printing the list in reverse order.
"""
v_cars = ['Bmw', 'audi', 'Toyota', "chai","bmw",'subaru']
v_cars.reverse()
print(v_cars)
"""
# Finding length of a list: 
"""
v_cars = ['Bmw', 'audi', 'Toyota', "chai","bmw",'subaru']
print(len(v_cars))
"""
#Exercise:1
v_place=["odisha","bhubaneswar","anugul","cuttactk","kuansh"]
print(v_place)
print("Sorted:--------------------------------------------------")
print(sorted(v_place))
print("original:--------------------------------------------------")
print(v_place)
v_place.reverse()
print('reverse:----------------------------------------------------')
print(v_place)
v_place.reverse()
print("reverse again:-----------------------------------------------")
print(v_place)
v_place.sort()
print("sort the list:---------------------------------------------")
print(v_place)
v_place.sort(reverse=True)
print("sort again:---------------------------------------------------")
print(v_place)
print("Length of the list:----------------------------------------")
print(len(v_place))












