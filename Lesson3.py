'''
    Conditional execution 
'''


x = 100
y = 100


if (x == y):
    if (x > y):                             # Nested conditional execution.
        print (" x is greater than y ")
    
    elif ( x >= y):
        print(" x is greater or equal to y")

    elif (x <= y):
        print(" x is less or equal to y")
    
    else:
        print (" x is less than y ")

else:
    print("X is not equal to Y.")

# Example problem And solution from Hackerrank

n = 8

if (n % 2 != 0):                    # modulus operator
    print("Weird   1")

elif (n % 2 == 0 and n>2 and n<5):
    print("Not weird  2")

elif (n % 2 == 0 and n>6 and n<20):
    print("Weird    3")

elif (n % 2 == 0 and n > 20):
    print("Not weird  4")