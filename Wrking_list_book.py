# Working with Lists:
# --------------------
# Example:1
"""
list_magicians = ["Alice","Scott","Alan","Jhony","Miller"]
for p_magician in list_magicians :
    print(p_magician)
"""
# Example:2
"""
list_magicians = ["Alice","Scott","Alan","Jhony","Miller"]
list_update_magicians = []
for p_magician in list_magicians :
    print(p_magician.title()+", Nice work!")
    print("we can't wait to see ur next trick"+" "+p_magician.title()+".\n")
"""
# Example:4 [storing the main list values in another empty list]
"""
list_magicians = ["Alice","Scott","Alan","Jhony","Miller"] #---------Main List
list_update_magicians = [] #---------------------------------Empty list
for p_magician in list_magicians :
    list_update_magicians.append(p_magician) #-----------Appending for loop values in empty list [But some error is there {follow example:5}]
    print(p_magician.title()+", Nice work!")
    print("we can't wait to see ur next trick"+" "+p_magician.title()+".\n")
    print(list_update_magicians)
"""
# Example:3
"""
#[IndentationError: expected an indented block]
v_magicians = ['alice','david','carolina']
for p_magician in v_magicians :
    print(p_magician)           # this is correct
#print(p_magician)              # this is wrong

#error

 [    print(p_magician)
        ^
IndentationError: expected an indented block]
"""
# Example:4 [Indenting Unnecessarily]
"""
v_magicians = ['alice','david','carolina']
    print(v_magicians)

#Error:

    print(v_magicians)
    ^
IndentationError: unexpected indent
"""
#Example:5
"""
list_magicians = ["Alice","Scott","Alan","Jhony","Miller"] #---------Main List
list_update_magicians = [] #---------------------------------Empty list
for p_magician in list_magicians :
    print(p_magician.title()+", Nice work!")
    print("we can't wait to see ur next trick"+" "+p_magician.title()+".\n")
    list_update_magicians.append(p_magician)  # -----------Appending for loop values in empty list
#   print(list_update_magicians)  # wrong Indent [Here new list is creating for every data in old list]
print(list_update_magicians) # Correct Indent
print("Thank you.")
"""

############################ MAKING Numerical Lists:


# using range() function
"""
#for value in range(1,10) : [this will print 1 to 9]
for value in range(1,11): #[this will print 1 to 10]
    print(value)
"""

# Using range() to make a list of Numbers
"""
v_rng_number = list(range(1,7))
print(v_rng_number)

#o/p [1, 2, 3, 4, 5, 6]
"""
#Example of even and odd numbers in a list
"""
v_evn_no = list(range(2,11,2))
v_odd_no = list(range(1,11,2))
print(v_evn_no)
print(v_odd_no)
"""

#Example
"""remove to test 1,2,3
sqr_values = []
"""
"""remove to test1,2,3
# or
for value in range(1,11) :
    sqr_value = value**2
    sqr_values.append(sqr_value)
"""
""" remove to test1,2,3
for value in range(1,11) :
    sqr_values.append(value**2)

print(sqr_values)

#o/p [1, 4, 9, 16, 25, 36, 49, 64]
"""
"""
v_list  = [1,2,3,4,5,6,7,8,9,0]
v_lst_sqr = []
print(min(v_list))
print(max(v_list))
print(sum(v_list))
for v_lst in range(1,11) :
    v_lst_sqr.append(v_lst**2)
print(v_lst_sqr)

"""
"""
v_str="Language:\n\tC\n\tJAVA\n\tSQL"
print(v_str)

list_magicians = ["Alice","Scott","Alan","Jhony","Miller"]

print(list_magicians)
#print(sorted(list_magicians))
del list_magicians[4]
list_magicians.remove("Alan")
print(list_magicians)
poped_magicians=list_magicians.pop(1)
print(list_magicians)
print(poped_magicians)
print(sorted(list_magicians))
"""

# Loop practice:
"""
list_magicians = ["Abhisek","Alice","Scott","Alan","Jhony","Miller","Alice"]
for v_Magician in list_magicians:
  # print(v_pr_list_Magi)
   # del list_magicians[1]

    print(v_Magician.title()+' '+"good job.\n")
v_Magician.remove("Alice")
print(v_Magician)

"""
"""
lst1=[]
lst2=[]
lst3=[]
for num1 in range(1,5):
    sqrt1=num1**2
    lst1.append(sqrt1)
print(lst1)

for num2 in range(2,11,2):
    sqrt2=num2**2
    lst2.append(sqrt2)
print(lst2)

for num3 in  range(1,10,2):
    sqrt3=num3**2
    lst3.append(sqrt3)
print(lst3)

print(min(lst3))
print(max(lst3))
print(sum(lst1))

"""
"""
sqrs=[]
for lst in range(1,11):
    sqr=lst**3
    sqrs.append(sqr)
print(sqrs)
"""
"""
sqrs=[value**2 for value in range(1,11)]
print(sqrs)
"""
"""
sqr_values=[value**2 for value in range(1,12,2)]
print(sqr_values)
"""

#Working with Part of a List
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:4])
print("\n2nd 3rd 4th")
#print(players[1:4])
#print(players[:4])
#print(players[-1])
#print(players[:])
plyrs=[value for value in players[1:5]]
print(plyrs)
print("New String.")
print(plyrs[-3:])
for i in plyrs:
    print(i)
"""
#Copying a List
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
frnds_food = my_foods[:]
print(frnds_food)
my_foods.append("Banana")
print(my_foods)
frnds_food.append("Apple")
print(frnds_food)
frnds_food.insert(1,"xyz")
print(frnds_food)
"""
# Example:2
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food=my_foods
my_foods.append("Banana")
print(my_foods)
friends_food.append("XYZ")
print(friends_food)
"""
"""
my_foods = ["pizza", "falafel", "carrot cake","banana cake","xyz","abcd"]
#print(my_foods[:3])
#print(my_foods[2:4])
print(my_foods[-3:])
"""
#Tuples: immutable list is called a tuple
"""
test_tpl = ("ASJS","jnf","vjfnvf")
print(test_tpl[0])
for tpl in test_tpl:
    print(tpl)
"""
# SET :
"""
v_set = {23,54,6,788,565,55,55,33}
print(v_set)
"""
"""
nums = [25,36,95,14,12,26] # question is delete : 95,14,12
del nums[2:5]
print(nums)
"""
#More on Variable:
"""
var = 4+5j
print(id(var))
print(type(var))
"""
# Converting float into int: 26th-March-2020
"""
num = 4.5
#print(num)
#print(type(num))
num2 = int(num) # converted to Int
print(num2)
print(type(num2))
num1 = float(num)
print(num1)
print(type(num1)) #converted to float
num3 = complex(num2,num1) # converted to complex
print(num3)
print(type(num3))
"""
#Example:
"""
print(1>2)
print(int(True))
print(int(False))
print(list(range(10)))
"""
# Dictionary or Map
dict={"Abhisek":"Asus","Biku":"OnePlus","Ara":"Samsung"}
print(dict.keys())
print(dict)
print(dict.values())















