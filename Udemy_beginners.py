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
"""
# Functions 
# Functions # Defining and calling function with no parameter
def f_demo() :
    print("Abhisek 1st Function in Python")
f_demo()

# Ex-2 # Defining and calling function with single parameter
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

def f_child(a,b) :
    c = a + b
    return c

def f_parent(d,e) :
    output = f_child(d,e)  #  calling the f_child function into f_parent function
    return output
print(f_parent(5,6))


