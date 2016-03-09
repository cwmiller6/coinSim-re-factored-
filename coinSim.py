#Author: Cole Miller
#Date: 3 Feb 2016

#remember, when using the random fuction, you need to import it since it is not in standard library of python
import random 

#Make a single variable 'result' and use the random.randint function to set it between 1 and 2
result = random.randint(1, 2)

#if the random int selected is 1, this will represent heads and will allow program to print heads
if result == 1:
	print("The coin lands on heads")
#if the random int selected is 2, this will represent tails and will allow program to print tails
if result == 2:
	print("The coin lands on tails") 