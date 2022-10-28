'''
    Conditional execution 
'''

x, y = 5, 10

if x != y :
    if(x < y):
        print("x is smaller than y? Yes, that's true !")
    elif(x > y):
        print("x is greater than y? No, that's false !")
    # elif x >= y:
    #     print("x is greater or equal to y? No, that's also false !")
    # else:           
    #     print("x is equal to y? No, false !")
else:
    print("x is equal to y")

