"""
Description: This program use different list to add and remove
Author: Dhruval patel
"""

my_list  = [1,2,3,4,5,'apple','lemon']

first_element = my_list[6]
print(first_element)

my_list[2] = "watermelon"
print(my_list)

# append
my_list.append(7)
print(my_list)

# insert
my_list.insert(5, 6)
print(my_list)

# remove
my_list.remove(4)
print(my_list)

# pop
poped_element = my_list.pop(5)
print(my_list)


# sort
my_list.sort(key=str)
print(my_list)

# reverse
my_list.reverse()
print(my_list)

list_animals  = ['Lion', 'Elephant', 'Tiger', 'Giraffe']
print(list_animals)

list_animals.append('Zebra')
print(list_animals)

list_animals.remove('Tiger')
print(list_animals)

poped_element = list_animals.pop()
print(list_animals)

tuple = (4, 5, 3)
print(tuple)
tuple1 = ("apple","bgmi","halo")
print(tuple1)

