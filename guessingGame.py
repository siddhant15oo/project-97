import random

number=random.randint(1,9)
numberChoose=input("choose a number between 1-9:")
chances=0
while chances<5:
    guess=int(input("guess again the number was wrong:"))

print (numberChoose)

if( numberChoose>number):
    chances=chances+1
elif(numberChoose<number):
        chances=chanses+1
elif(numberChoose==number):
            print("hooray!you got the number")
    