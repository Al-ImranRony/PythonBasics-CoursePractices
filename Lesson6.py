'''
Function in python
'''

print()
type()
int()
float()


def showSentence(c):
    count = c
    for i in range(10):
        count += i+1

    return count

returnedC = showSentence(0)
print(returnedC)









# givenWord = "AbrakaDabra"

# maxLetter = givenWord[0]

# def maxLetterOfGivenWord(word)-> str:
#     for letter in word:
#         print(letter)
#         if letter > maxLetter:
#             maxLetter = letter

#     return maxLetter

# s = maxLetterOfGivenWord(givenWord)
# print(s)