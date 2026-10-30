"""
###Assignment Questions:

##Question 1: Enumerate with List
Given the list:
fruits = ["apple", "banana", "cherry", "mango"]

Use enumerate() to print each fruit with its index number.
Output format example:
0 apple  
1 banana  
2 cherry  
3 mango


##Question 2: Zip with Two Lists
Given two lists:
students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

Use zip() to print each student name along with their score.
Example Output:
Rahim scored 85  
Karim scored 90  
Ayesha scored 78


##Question 3: Tuple and Loop
Create a tuple of 5 subjects.
Using a for loop, print each subject one by one.


##Question 4: Set Operations
Given the sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
Print the common elements using set operation.
Print the unique elements of set1.



##Question 5: Dictionary with Enumerate
Given the dictionary:
marks = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85
}
Using a loop and enumerate():
Print the subject number, subject name, and marks.

Example Output:
1 Math: 80  
2 Physics: 75  
3 Chemistry: 85
"""


                 ###Answer###

#Question 1: Enumerate with List
fruits = ["apple", "banana", "cherry", "mango"]
for idx,item in enumerate (fruits): #idx means index which normally start from 0.
  print(idx,item)
#0 apple
#1 banana
#2 cherry
#3 mango

#Question 2: Zip with Two Lists
students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

for i, j in zip(students,scores): #here i refers student names and j refers students scores.
  print(f"{i} scored {j}")
#Rahim scored 85
#Karim scored 90
#Ayesha scored 78


#Question 3: Tuple and Loop
sub = ("Math", "Phy", "Chem", "Bio", "Eng") #let these arw the five subjects
for i in sub:
  print(i)
#Math
#Phy
#Chem
#Bio
#Eng


#Question 4: Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
common = set1.intersection(set2) #this show only common elements
print("Common values are:",common)
#Common values are: {4, 5}

unique = set1.difference(set2) #show Only unique elements of set1
print("unique values of Set1 are:",unique)
#unique values of Set1 are: {1, 2, 3}



#Question 5: Dictionary with Enumerate
marks = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85
    }

for idx, (sub,score) in enumerate(marks.items(), start=1): #here idx = index, use items as(sub and Scores) and index start from 1.
    print(f"{idx} {sub}: {score}")
#1 Math: 80
#2 Physics: 75
#3 Chemistry: 85