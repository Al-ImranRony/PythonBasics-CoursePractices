'''
Function in python
'''


def showSentence(c):
    count = c
    for i in range(10):
        count += i+1

    return count

returnedC = showSentence(0)
print(returnedC)



givenWord = "AbrakaDabra"

def maxLetterOfGivenWord(word)-> str:
    maxLetter = givenWord[0]
    for letter in word:
        # print(letter)
        if letter > maxLetter:
            maxLetter = letter

    return maxLetter

s = maxLetterOfGivenWord(givenWord)
print("The max valued letter we have found is:", s)