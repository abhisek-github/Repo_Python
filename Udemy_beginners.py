#CHAPTER - 6 [COMMENT AND MATH OPERATOR]
#1. COMMENT
"""
v_ename='Abhisek'
v_sal=2500

print(v_ename)
print(v_sal) #this will print the v_sal value in number
print(v_ename+" "+str(v_sal)+" "+"per month") # this will print v_sat in string
"""

#2.MATH OPERATOR
"""
v_a=3
v_b=4
print(v_a+v_b)
v_a +=5 #re-assignment to v_a
# or v_a = v_a + 5
print(v_a)
print(6//-1)
print(10%-6)
print((9-7)*2**3+10%6//-1*2-1)
"""
#   Strings and Escape Sequences
"""
v_str1=  "Who is \"Abhisek Mohanty\" ?"
print(v_str1)
"""
# Accessing By Index
"""
v_str_in="Abhisek"
print(v_str_in[0])
print("abhisek"[2]) # "abhisek" 0 1 2 3 4 5 6
"""
# Slicing a String
"""
var_s="Abhisek"
print(var_s[3:])
print(var_s[:2])
print(var_s[2:5])

print("Apple"[:3])
print("Apple"[3:5])
"""
# String Method
"""
v_ename="Scott"
print(len(v_ename)) # len() Method

v_deptno=10
print("Abhisek" + " office" + " deptno" + " is" +" " + str(v_deptno))

v_lower = "abhisek"
v_upper = "MOHANTY"
print(v_lower.upper() +" "+ v_upper.lower().title()) # output : ABHISEK Mohanty

# print() : %s format operator . Here %s works as a place holder

v_state = "Odisha"
v_country = "India"

print("Abhisek Mohanty Is from %s , %s."% (v_state,v_country)) # o/p Abhisek Mohanty Is from Odisha , India.
"""

# Input()
"""
occupation = input("what is your occupation : ").title()
city = input("which city do you live in : ").title()
age = input("how old are you : ")
print("So you are a %s from %s and you are %s years old ."%(occupation,city,age)) # O/P So you are a Software Engineer from Bangalore and you are 25 years old .
"""
#.Section :4 Conditionals and Flow control

# Flow controls and comparators
"""
v_eql = 1==7
print(v_eql)   # False

v_nt_eql = 3 != 4
print(v_nt_eql) # True

v_grt = 7 > 4
print(v_grt) # True

v_grt_eql = 4 >= 5
print(v_grt_eql) # False

v_les = 4 < 5
print(v_les) # True

v_les_eql = 7 <= 5
print(v_les_eql) # False
"""

# Boolean Operator
"""
v_t = True and True
v_t1 = True and False
v_t2 = False and False
print(v_t)
print(v_t1)
print(v_t2)

print(not False and not True or False) # o/p False
"""
"""
operation order
print(not False and not True or False)
        True    and False   or False
            False           or False
                False
"""
# if , Else and Elif
"""
if 5 != 6:
    print("5 equal to 6")
else:
    print("5 doesn't equal to 6")
# Ex-2
if 5 == 6:
    print("5 equal to 6")
else:
    print("5 doesn't equal to 6")
"""
"""
if 1 == 2:
    print("Don't print this")
elif 1 != 2:
    print("print this")
#elif 1 != 2:   # we can add no of elif statement in If else statement
#    print("don't print")
else:
    print("Don't print this either")
"""
""" Example_Dummy
v_name_DOB = input("What's your name with DOB : ")
v_state_pin = input("Where are you from ,Give your state and pin : ")
if   v_name_DOB == "Abhisek1994" :
    print("You are Abhisek Mohanty")
    
elif  v_state_pin == "Odisha756100" :
    print("You are Abhisek Mohanty")
else:
    print("Enter a valid input , you are not recognise by me.")
"""

# Functions 
# Functions # Defining and calling function with no parameter
"""
def f_demo() :
    print("Abhisek 1st Function in Python")
f_demo()
"""
# Ex-2 # Defining and calling function with single parameter
"""
def f_single_parm(a) :
    print(a)
f_single_parm(7)
f_single_parm('h')
"""
# Ex-3 # Defining and calling function with multiple parameter
"""
def f_multi_param(a,b,c) :
    d = a ** b
    print(d + c)
f_multi_param(2,3,4)
"""
# Ex-4 Calling a function inside of another function.
"""
def f_child(a,b) :
    c = a + b
    return c

def f_parent(d,e) :
    output = f_child(d,e)  #  calling the f_child function into f_parent function
    return output
print(f_parent(5,6))
"""
# Ex -5
"""
def f_print() :
    print("This is a Function")

def f_first_int(a,b):
    c = a * b
    return c
def f_second(d,e):
    f = d * e
    return f
def f_cal(p1,p2,p3,p4):
    print(f_second(f_first_int(p1,p2),p3 * p4))
f_print()
f_cal(2,3,4,2)
"""
# Importing Modules
# Generic Import
"""
import random
print(random.randint(1,10))

# Function import

from random import randint
print(randint(20,30))
"""
# Built - In function
# abs()
"""
print(abs(-9))
print(abs(0))
print(abs(5))
"""
# type()
"""
print(type(1))
print(type(3.5))
print(type("Abhisek"))
print(type(True))
"""
# max()
"""
print(max(3,4,5,6))
print(max(3.5,6.8,6.5))
print(max("ab","cd","xa"))
print(max("a","b","z"))
"""
# min()
"""
print(min(3,4,5))
print(min("a","b","g"))
print(min(5.7,8.9,3.5))
"""
#Section - 6

#Lists  # index re-assign  # .insert() # .remove()
"""
v_list = ["Abhisek","mani","sai",8]
print(v_list[1])
print(v_list[1].title() +" and "+ v_list[2].title())
print(v_list[3])

v_list[3]="Ashmin"
print(v_list[3])
v_list.append("Nag")
v_list.insert(2,"Shobha")
print(v_list)
v_list.remove("Abhisek")
print(v_list)
"""
# List Slicing
"""
v_list_sli = [2,3,4,5,6,7]
v_list_sli_chr = ["A","B","C","D","E","G"]
print(v_list_sli[2:]) # o/p  [4, 5, 6, 7]
print(v_list_sli[:1]) # o/p [2]
print(v_list_sli_chr[2:5]) # o/p ['C', 'D', 'E']
print(v_list_sli_chr[:3]) #o/p ['A', 'B', 'C']
print(v_list_sli_chr[0:]) # o/p ['A', 'B', 'C', 'D', 'E', 'G']
#print(v_list_sli[len(v_list_sli)]) - error Index out of range
"""
# .index()
"""
v_indx = ["A","B","C","D","E","F"]
print(v_indx.index("D"))
v_index_fist = [1,1,0,1,1,1,0]
print(v_index_fist.index(0))
print(v_index_fist.index(1))
"""
# .pop()
"""
v_pp = ["A","B","C","D","E","F"]
v_pp.pop(3)
print(v_pp)
v_pp.pop()
print(v_pp)
"""
# For loop and Tuples
# Tuples
"""
v_tupl = (2,"abhisek","sai","manideep","shiva",1)
print(v_tupl)
print(v_tupl[1].title())
#v_tupl.append("Nag") [Error = AttributeError: 'tuple' object has no attribute 'append']
#v_tupl.insert(3,"AAA") [AttributeError: 'tuple' object has no attribute 'insert']
print(v_tupl[:3])
"""
# For Loop
# Ex - 1
"""
v_List = ["A","B","C","D","E","F"]
v_tuple = (2,"abhisek","sai","manideep","shiva",1)
print("1st For Loop")
for elements in v_List :
    print(elements)

print("2nd For loop")
for items in v_tuple :
    print(items)
"""
#Ex - 2
"""
v_list = [2,3,4,5]
empty = []
v_tup = ("Let"," it "," be ")
song = ""
for nums in v_list :
    empty.append(nums*4)

for string in v_tup :
    song +=string
print(empty)
print(song)
"""
# Dictionary

v_dict = {8: "abhisek" ,2: "ashmin",3: "manideep"}
print(v_dict[8].title())
print(v_dict[2].title())
print(v_dict[3].title())

v_dict_str = {"A": 2,"B": 4,"C": 40}
print(v_dict_str["B"])
print(v_dict_str["c"])






