'''
Arithmetic operators
'''

a, b = 3, 7

addition = a + b
subtraction = a - b
multiplication = a * b
powerValue = b ** a   # 7 to the power 3
division =  b / a
divWithIntValue = b // a
modulus = b % a

print ("Division of a and b: ", division)
print("Division of a and b for integer value only : ", divWithIntValue)
print("Power value of b: ", powerValue)
print("Modulus: ", modulus)

#Augmented assignment operation
a *= 3
print(a)