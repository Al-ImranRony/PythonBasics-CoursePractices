'''
List Comprehension - Lesson 9
'''

# One functional way to create a list is using map objects 
aList = [1, 9, 36, 81, 144]

def getSquaredNums(num):
    return num * num
sNums = map(getSquaredNums, aList)
asList = list(sNums)
print(asList)

# Create list using for loop
bList = []          # Declare an empty list

for num in range(5):
    bList.append(num)

# Now using the same process for list comprehension
cList = [num for num in range(5)]

print(bList, " - ", cList)          # Result will be similar

# Modify item on list creation using comprehension
mList = [num*3 for num in range(5)]
msList = [num * num for num in mList]           # Can Modify existing list also
sList = [letter.upper() for letter in "Comprehension"]
print(sList)

# Conditionals on list
mcList = [num * num for num in mList if num%2 == 0]
print(mList, msList, mcList)

# Nested comprehension 
matrix = [[num for num in range(5)] for i in range(3)]
print(matrix)