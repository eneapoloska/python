print("Hello World!")
x = "Hello Python"
print(x)
y = 42
print(y)
############################################################
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
############################################################

##########################################################################################################################################

#Tuples
# A type of data that is immutable (can't be modified after its creation) and can hold a group of values.
#Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[2])		# output: Bruce
##############dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)
##########################################################################################################################################

#List
# A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']
#################################################################################################################################

#Dictionaries 
#A group of key-value pairs. 
# Dictionary elements are indexed by unique keys which are used to access values. 
# When you're ready, you can find more built-in dictionary methods here.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']} 
###############################################################################################################################

#Common Functions
# If we're ever unsure of a value or variable's data type, we can use the type function to find out. 
# For example:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>
#For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), 
# we can use the len function to get the length:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11
##############################################################################

print(type(24))
print(type(3.9))
print(type(3j))
####################################

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))
#############################

from cmath import pi
from msilib import sequence
from multiprocessing.heap import Arena
import random
print(random.randint(150,86394)) # provides a random number between 2 and 5

mosha = 3
print('my sons name is', mosha)

#print("Hello " + 42)			# output: TypeError
print("Hello " + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
############################################################

#####String Literals
# Strings are any sequence of characters (letters, numerals, ~($/}\#, etc.) enclosed in single or double quotes. 
# We can display a string like this:
print("this is a sample string")

######Concatenating Strings and Variables with the print function
#######String Interpolation
first_name = "Zen"
last_name = "Coder"
age = 33
print(f"My name is {first_name} {last_name} and I am {age} years old.")
##################################################################

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
#####################################################################

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27
###########################################################

x = "hello world"
print(x.title())
# output:
"Hello World"
########################################################

#####################LIST<<<

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

#In Python, the elements of a list do not have to be of the same data type.
# A list can be a mixture of any Python data types, including, tuples, strings,
#  numeric, and even a list itself (a list within a list). An example:

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)
######################################

#Accessing Values<<<<<<<<<<<<<<<<<

#Back to the dresser analogy, imagine that each drawer is numbered starting with 0. 
# Say the first drawer( index of 0) has 'documents' inside, the second drawer (index 1) has 'envelopes' inside, and so on. 
# Each drawer holds a number, also known as the index (which serves as the unique address that points to each of our items inside the drawer). 
# You can access the items in the drawer like below:
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

#Manipulating Lists<<<<<<<<<<<<<<<

# Here's a useful example of a method that we will use to manipulate lists:
#<list>.append(<new_element>)###
#Appends a new item onto the end of the given list. You can pass any data type into this function.

x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]

#It's important to know that Python uses [ ] characters to return a copy of the list, constrained to the specified indices. 
# This can be thought of as behaving like the slice function in JavaScript. 
# The starting index and ending index should be separated by the ":" character.

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];

#For information on other available list methods, read the docs.

#List Built-in Functions---------------------
# Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequences, including tuples and strings. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly used sequence function:
# len(sequence): Returns the number of items in a sequence.

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

#Some built-in functions for sequences:
# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# There are a few other useful built-in functions. Find them here.

# List Built-in Methods---------------------
#Below is an example of a built-in list method. These methods are specific to lists versus other sets, much like the string methods shown in the previous tab.

#list.append(value)

my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list)
# output:
# [1,5,2,8,4,7]

#The following are some commonly used list methods:
# list.extend(list2) adds all values from a second sequence to the end of the original sequence.
# list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
#list.index(value) returns the index position in a list for the given parameter.

#These are just some of the things you can do to manipulate or extract information from a list. 
# Click here to learn more about other built-in functions you can use with a list.


#######################Tuples<<<<<<<<<<<<<<<<<<<<<<<
#_____________________________________________________#
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"
print(tuple_letters)
#A tuple can be used to group any number of items into a single compound value.
#  Syntactically, a tuple is a comma-separated sequence of values. 
# Although it is not necessary, it is conventional to enclose tuples in parentheses.______________<---

dog = ("Canis Familiaris", "dog", "carnivore", 12)

print(dog[2])
#result is: carnivore

#If we try to use item assignment to modify one of the elements of the tuple, we get an error:
###############dog[0] = "X"<---------
#TypeError: 'tuple' object does not support item assignment
#Like strings, tuples are immutable. 
# Once Python has created a tuple in memory, it cannot be changed. 

# But we can add and slice tuples. See example below:
dog = dog + ("domestic",)
print(dog)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:2] + ("man's best friend",) + dog[4:]
print(dog)
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

#Built-in Tuple Functions
#Here are a few of the most commonly used tuple functions. 
# You'll recognize many of these functions and methods from the list tab. 
# Tuples are just sequences with slightly different characteristics from lists.

#len(sequence): Returns the length of the given tuple.

x = (1,5,6,9,2)
print(len(x))
# output:
# 5
#print(max(x))----------------<--------
#You may recognize some of these built-in functions for sequences:
#max(sequence) returns the largest value in the sequence
#sum(sequence) return the sum of all values in sequence
#enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
#map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
#min(sequence) returns the lowest value in a sequence.
#sorted(sequence) returns a sorted sequence

#You'll find that many of the built-in functions that work with lists can also work with tuples. 
# Find the built-in tuple methods here.

#Tuple as return Values------------------
#Functions can always only return a single value, but by making that value a tuple, we can effectively group together as many values as we like, and return them together. This is very useful — we often want to know some highest and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the day.
#For example, we could write a function that returns both the circumference and the area of a circle of radius r:

def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
#-------------------????????????????????????????????????????
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * pi * r
    a = pi * r * r
    print(c, a)
    return (c, a)
#-------------------------------------------------???????????????????

#Why tuples?
#The following is a little extra information on tuples. Read on if you wish.
# It's okay if you don't understand use cases for tuples at this point. 
# Most students finish this tab wondering "Why would I ever want to use a tuple? 
# It's like a list but less flexible!" 
# At first glance, tuples might seem like they're more trouble than they're worth.
# In reality, tuples can store grouped information in such a way that any consumer of your code,
#  i.e. other developers, can't modify sets of data that should be kept constant. 
# Let's take an example.
# I've written a code base called "Anna's Cool Python Language Library", and included in my library is a function, 
# that, when invoked, returns all the translations of a word in 3 different languages. 
# My code will return the word in 3 different languages, English, Spanish, and French. 
# English will always be at index 0, French at index 1, and Spanish at index 2. 
# My results might look like so:

import language
print(language.translate(dog))
# output would look something like: ("dog", "chien", "perro")

# With a tuple, I can write the rest of my library with the assumption that each language will be found at its original position. 
# This guards against errors and is an understood communication to the developer 
# that order and number of entries are important and should not be modified. 
# Understanding when to use tuples is an advanced concept. It's good to know and important to be able to recognize 
# why another developer might have chosen to use it in their code. 
# You may not find a use case yourself while you're still learning the basics.

################Dictionary<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#_________________________________________________________________________#
#A Dictionary is another mutable set type that can store any number of Python objects, 
# including other set types. Dictionaries consist of pairs (called items) of keys and their corresponding values. 
# While this data structure is known as a dictionary in Python, 
# you'll see the same structure referred to as an associative array or hash table in other languages. 
# In general, hash table is the most generic term.

#The following is a general summary of the characteristics of a Python dictionary:
    #A dictionary is an unordered collection of objects.
    #Values are accessed using a key.
    #A dictionary can shrink or grow as needed.
    #The contents of dictionaries can be modified.
    #Dictionaries can be nested.
    #Sequence operations such as slice cannot be used with dictionaries.

#Creating Dictionaries
# Creating a dictionary in Python is a little bit like creating any other set. 
# There are 3 types of sets in Python. 
# You've already learned about lists and tuples. W
# hile lists are enclosed by brackets – [], 
# and tuples are enclosed by parenthesis – (), dictionaries are enclosed by braces – {} 
# and use keys to track position rather than an index. 
# Below are a couple of techniques you'll find useful when building dictionaries.

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
#In the example above, we created two dictionaries in two different ways:
    #1.Using literal notation. The key-value pairs are enclosed by curly brackets. The pairs are separated by commas. 
    # The first value of a pair is a key, which is followed by a colon character and a value. 
    # The "Sun" string is a key and the "Sunday" string is a value.
    #2.Creating empty dictionary and adding some values. 
    # The keys are inside the square brackets, the values are located on the right side of the assignment.
#Each key in a dictionary must be unique. 
# If you make an assignment using an existing key as the index, ,<------------------
# the old value associated with that key is overwritten by the new value. <_-------------------
# You can use this characteristic to an advantage in order to modify an existing value for an existing key.

#####################Accessing Values
#To access the values of a dictionary, 
# you can use the familiar square brackets along with the key to obtain its value.
print(capitals["dnk"])
print(weekend["Sat"])


###########################Removing Values################
#There are 2 ways to remove a key:value pair from a dictionary. 
value_removed = capitals.pop("svk") # will remove the key 'svk' and return it's value
del capitals["dnk"] # will delete the key, and not return anything

###Nested Dictionaries

########Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples. 

context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

print(context["questions",{"id"}])

#Built-in Functions and Methods--------------------------
#Python includes the following standalone functions for dictionaries:

    #cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
    #len() - give the total length of the dictionary.
    #str() - produces a string representation of a dictionary.
    #type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.

#Python includes the following dictionary methods:
#(either dict.method(yourDictionary) or yourDictionary.method() will work)

    #.clear() - removes all elements from the dictionary
    #.copy() - returns a shallow copy dictionary
    #.fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
    #.get(key, default=None) - For key key, returns value or default if key is not in dictionary.
    #.items() - returns a list of dictionary's (key, value) tuple pairs.
    #.keys() - return a list of dictionary keys.
    #.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
    #.update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
    #.values() - returns list of dictionary values.



#################Conditional statements################
#Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.  
# These statements control the flow our code is executed by the interpreter.  
# In Python, the keywords for conditional statements are if, elif, and else. 
# Here are some examples:
x = 12
if x > 50:
	print("bigger than 50")
else:
	print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
if x > 10:
	print("bigger than 10")
elif x > 50:
	print("bigger than 50")
else:
	print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
	print("smaller than 10")
# nothing happens, because the statement is false  

#Comparison and Logic Operators<<<<<<<<<<<<<<<
#__________________________________________________-#
#Here is a table of the comparison operators you can use in your Python programs.
#Operator 	Description 	Example
#  == 	Checks if the value of two operands are equal 	1 == 2 => False * 1 == 1 => True
#  != 	Checks if the value of two operands are not equal 	1 != 2 => True * 1 != 1 => False
#  > 	Checks if the value of left operand is greater than the value of right operand 	1 > 2 => False * 2 > 1 => True
#  < 	Checks if the value of left operand is less than the value of right operand 	1 < 2 => True * 2 < 1 => False
#  >= 	Checks if the value of left operand is greater than or equal to the value of right operand 	1 >= 2 => False * 2 >= 2 => True
#  <= 	Checks if the value of left operand is less than or equal to the value of right operand 	1 <= 2 => True * 2 <= 2 => True
#  and 	Checks that each expression on the left and right are both True 	(1 <= 2) and (2 <= 3) => True
(1 <= 2) and (2 >= 3) => False
(1 >= 2) and (2 >= 3) => False
#  or 	Checks if either the expression on the left or right is True 	(1 <= 2) or (2 >= 3) => True
(1 <= 2) or (2 <= 3) => True
(1 >= 2) or (2 >= 3) => False
#  not 	Reverses the true-false value of the operand 	not True => False
not False => True
not 1 >= 2 => True
not 1 <= 2 => False
not (1 <= 2 and 2 >= 3)  => True
not 1 <= 2 and 2 >= 3 => False

####################LOOPS##########################
####For Loops with Range
#Start - Stop - Step
# Note that if you need to specify an increment other than +1, all three arguments are required.
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

for i in range(50):
    print(i)
#----------------------#

##########For Loops through Strings
#Since a loop can be used on any sequence, you can access each value of a string individual with loop.

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

#####For Loops through Lists
####If we want to iterate through a list, 
# we could use the range function and send in the length of the list as the stopping value, 
# but if we are not interested in the index values and want to just see the values of each item in the list in order, 
# we can actually loop to get the values of the list directly!
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
my_list = ["abc", 123, "xyz"]
for v in my_list:
    print(v)
# output: abc, 123, xyz

#######For Loops through Tuples
#We can iterate through a tuple in the same ways we iterate through a list.
dog=("hami", " i zi ", "cicija", 2 ) #mund te behet dhe me "2"
for data in dog:
    print(data)

############For Loops through Dictionaries
#Dictionaries are also iterable. When we iterate through a dictionary, 
# the iterator is each of the keys of the dictionary.
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

#That means if we want the values of our dictionary, we might do something like this:
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

#Dictionaries also have a few additional methods that 
# allow us to iterate through them and have the keys and/or values as the iterator. 
# Test these out to get a better understanding:
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

#to iterate through the values
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond

#to iterate through both keys and values
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
for key, val in capitals.items():
    print(key, " -> ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc



###########While Loops<----------------------------------
#While loops are another way of looping while a certain condition is true.
#Remember this for loop?
for count in range(0,5):
    print("looping =", count)

#We can rewrite it as a while loop:
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

#The basic syntax for a while loop looks like this:
#    while <expression>:
        # do something, including progress towards making the expression False. 
        # Otherwise we'll never get out of here!

##########Else?????????????????????????????????????
#There are certain conditions that we give for every loop that we have, 
#but what if the condition was not met and we still would like to do something if that happens? 
#We can then use an else statement with our while loop. 
#Yes, that is right, else in a loop.

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
#Note that this else code section is only executed if the while loop runs normally and its conditional is false 
# (whether we never entered the while loop, or we did but eventually the conditional changed from true to false). 
# If instead our while loop is exited prematurely because of a break or return statement, 
# then the else code section will never be executed.


##############Loop Control<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#________________________________________________________________#
#We were introduced to control flow in the previous tabs with if and else statements. 
# Loops, breaks, and continues are all a part of control flow as well. 
# Control flow is the cornerstone of most programming languages.
#When you want finer control over your loops, use the following statements to do so.

#>>>>>>>>>>>>Break
#The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. 
# The break statement can be used in both while and for loops.
# The most common use for the break is when some external condition is triggered, 
# requiring a hasty exit from a loop.
# When loops are nested, a break will only exit from the innermost loop.
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r
#Notice that when the loop got to the letter "i", we stopped looping.


#>>>>>>>>>>>Continue
#The continue statement immediately returns control to the beginning of the loop. 
# In other words, the continue statement rejects, or skips, 
# all the remaining statements in the current iteration of the loop, 
# and continues normal execution at the top of the loop.
#The continue statement is very useful when you want to skip specific iteration(s), 
# but still keep looping to the end.
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

#Basic - Print all integers from 0 to 150.

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines

def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')

counting_dojo()

minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))


for i in range(1,101):
    if i%5==0:
        print("codin")
    elif i%10==0:
        print("cd")
    elif i%5==0 and i%10==0:
        print("cd")
    else:
        print(i)

count  
    while i <= 100 
    i = i + 5 
    print i 

for x in range(1, 101):
    if x % 5 == 0:
        print('Coding')
    if x % 10 == 0:
        print(' Dojo')
    elif
        print(x)

for i in range(1,101):
  if i%10==0:
      print("coding dojo") 
       
  if i%5==0 and i%10!=0:
      print("coding")

sum=0
for i in range(0,500000+1):
    if i%2==1:
    sum=sum+i
print(sum)