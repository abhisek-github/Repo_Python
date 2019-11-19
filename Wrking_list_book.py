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
#for value in range(1,10) : [this will print 1 to 9]
for value in range(1, 11): #[this will print 1 to 10]
    print(value)
