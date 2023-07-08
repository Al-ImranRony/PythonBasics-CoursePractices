'''
List in Python
'''


# Declare, access, change

# IDs/Indexes    0         1        2        3        4
khadokList = ["Forhad", "Zahed", "Shakil", "Rafi", "Zuthi"]

khadokNumber = [11, 222, 33, 444, 55]
variableList = [9, 9.0, 9.2349879230987, 'adskhhku', True]

print(variableList)

arrList = [1] * 50

khadokNumber[4] = 5555
print("Updated khadok number: ", khadokNumber)

# String as a list
firstKhadok = ['F', 'o', 'r', 'h', 'a', 'd']
print(firstKhadok)


'''
List methods  
'''
# 1.
khadokList.append("Rony")
print(khadokList)

# 2.
khadokList.insert(0, "Rony")
print(khadokList)

# 3.
# khadokList.pop()
# print(khadokList)

# 4.
cnt = khadokList.count("Rony")
print(cnt)

# 5.
print(len(khadokList))

# 6.
khadokList.sort(reverse=True)
print(khadokList)

# 7.
khadokList.remove("Rony")
print(khadokList)

# 8.
khadokList.clear()
print(khadokList)


