'''
Loops and Iterations
'''

totalMonths = 0

for year in range(2010, 2023):
    print(year, "->")

    for month in range(1, 13):
        print( month )

        totalMonths += 1
    
print(totalMonths)


'''
While loop
'''

totalMonths = 0
year = 2010

while (year < 2023):
    totalMonths += 12
    year += 1   #2023

print(totalMonths)