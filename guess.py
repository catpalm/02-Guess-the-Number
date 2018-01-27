# !/usr/bin/python3

import sys, random

assert sys.version_info >= (3, 4), "This script requires at least Python 3.4"



guess_range = 20
tries = 0

print('Try and find the number between one and twenty.')
print('But first tell me your name')
person = input('Enter Name:')
print('Excellent', person, ', now I know your name!')
print('Now try to find the hidden number within 10 tries')


number = random.randint(1, guess_range)




try:




	while tries < 10:
		guess = input()
		guess = int(guess)

		tries = tries + 1

		if guess < number:
			print('Sorry but you are too low', person)

		elif guess > number:
			print('Unfortunately you are too high', person)

		if guess == number:
			break

	if guess == number:
		print('Congratulations, you have won', person)

except ValueError:
		print('Im afraid I cant let you do that, Dave')

