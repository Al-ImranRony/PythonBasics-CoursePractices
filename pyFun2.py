'''
Making patterns with python loops
'''

print("*")
print("###")
print("$" * 5)

for x in range(7):
    print("L" * x)

n = 7
spaces = n-1

for i in range(0, n):

    for j in range(0, spaces):
        print(end=" ")
    spaces -= 1

    for j in range(0, i+1):
        print("* ", end="")

    print("\r")

