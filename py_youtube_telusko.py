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













