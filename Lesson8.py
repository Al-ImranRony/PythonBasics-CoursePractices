'''
String methods
'''


intInput = input("Give an integer number as a input: ")
intInputVar = int(intInput)

print("type(intInput)" + " " + intInput + " " + "42989")

#Formatted string
formattedStringInput = f'Showing {intInputVar} integer value as a string.'
print(formattedStringInput)

# len function for string
print(f'Length of the given string is : {len(intInput)}')

pySentence = "Fundamental of python"
print(pySentence.upper())
print(pySentence.lower())
print(pySentence.find('of'))
print(pySentence.replace(" of", " learning in"))

# Checking through the full string using 'in' operator, Return true if finds a word in sentence 
if 'Fundamental' in pySentence:                        
    print(pySentence.replace("Fundamental", "Basics"))

