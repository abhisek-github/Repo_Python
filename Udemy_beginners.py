#CHAPTER - 6 [COMMENT AND MATH OPERATOR]
#1. COMMENT
"""
v_ename='Abhisek'
v_sal=2500

print(v_ename)
print(v_sal) #this will print the v_sal value in number
print(v_ename+" "+str(v_sal)+" "+"per month") # this will print v_sat in string
"""
"""
#2.MATH OPERATOR
v_a=3
v_b=4
print(v_a+v_b)
v_a +=5 #re-assignment to v_a
# or v_a = v_a + 5
print(v_a)
print(6//-1)
print(10%-6)
print((9-7)*2**3+10%6//-1*2-1)

#   Strings and Escape Sequences

v_str1=  "Who is \"Abhisek Mohanty\" ?"
print(v_str1)

# Accessing By Index

v_str_in="Abhisek"
print(v_str_in[0])
print("abhisek"[2]) # "abhisek" 0 1 2 3 4 5 6

# Slicing a String

var_s="Abhisek"
print(var_s[3:])
print(var_s[:2])
print(var_s[2:5])

print("Apple"[:3])
print("Apple"[3:5])

# String Method

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
occupation = input("what is your occupation : ").title()
city = input("which city do you live in : ").title()
age = input("how old are you : ")
print("So you are a %s from %s and you are %s years old ."%(occupation,city,age)) # O/P So you are a Software Engineer from Bangalore and you are 25 years old .



