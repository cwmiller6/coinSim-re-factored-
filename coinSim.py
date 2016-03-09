#Author: Cole Miller
#Date: 3 Feb 2016

#remember, when using the random fuction, you need to import it since it is not in standard library of python
import random 

#Enchancment for while loop (Re-Factoring Git Assignment): 
spin = True

while spin == True:
	result = random.randint(1, 2)
	again = raw_input("Would you like to flip again? (y or n)\n>".lower())
	if again == 'y':
		#if the random int selected is 1, this will represent heads and will allow program to print heads
		if result == 1:
			print("The coin lands on heads")
		#if the random int selected is 2, this will represent tails and will allow program to print tails
		if result == 2:
			print("The coin lands on tails") 
	if again == 'n':
		print("Thanks for flipping!")
		spin = False 
