def reverse(lst):
   result = []

   for element in lst:
       result.insert(0, element)

   return result

# print(reverse([1, 2, 3, 4]))


# creating a list using the list constructor. Lists are objects in Python
list1 = list()   # creates an empty list
list2 = list([2, 3, 4])  # creates a list with the 3 elements
list3 = list(["red", "green", "blue"]) # create a list of strings
list4 = list(range(3, 6)) # create a list with elements 3, 4, and 5
list5 = list("abcd") # create a list with characters, a, b, c, d
'''
print(list5)

list1 = []
print ("Enter a number: ")
for i in range (10):
    list1.append(eval(input()))
print(list1)

s = input("Enter 10 numbers separated by spaces from one line: ")
items = s.split()
list2 = [eval(x) for x in items] # this is a list comprehension
print(list2)


import random
list1 = [30, 1, 2, 2, 43, 56]
print(list1[random.randint(0, (len(list1) - 1))])
'''

list1 = [1, 2, 3, 4, 5, 6]
for i in range (1, 6):
    list1[i] = list1[i - 1]
print(list1)