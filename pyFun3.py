'''
HW- Dividing the pizza using loops and functions

A plate of noodles = 1200 pieces
Number of pizza lover = 5
Slices receiver sequence Forhad->Zahed->Shakil->Rafi->Juthi
'''


totalPieces = 1200
forhadsPlate = zahedsPlate = shakilsPlate = rafisPlate = juthisPlate = 0


for sliceNumber in range(1, totalPieces+1):

    if (sliceNumber%5 == 1):
        forhadsPlate += 1
    elif (sliceNumber%5 == 2):
        zahedsPlate += 1
    elif (sliceNumber%5 == 3): 
        shakilsPlate += 1
    elif (sliceNumber%5 == 4):
        rafisPlate += 1
    else:
        juthisPlate += 1

print("Forhad's plate have", forhadsPlate, "slices.")
print("Zahed's plate have", zahedsPlate, "slices.")
print("Shakil's plate have", shakilsPlate, "slices.")
print("Rafi's plate have", rafisPlate, "slices.")
print("Juthi's plate have", juthisPlate, "slices.")

