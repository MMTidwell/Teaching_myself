import random

# safely make an int
# limit guesses
# too high message
# too low message
# play again

def game():
	secret_number = random.randint(1, 10)
	guesses = []

	while len(guesses) < 5:
		try:
			guess = int(raw_input("Guess a number between 1 and 10: "))
		except ValeError:
			print("{} isn't a number!".format(guess))
		else:
			if guess == secret_number:
				print("You got it!! My number was {}. ".format(secret_number))
				break
			elif guess < secret_number:
				print ("My number is higher than {}.".format(guess))
			else:
				print("My number is lower than {}.".format(guess))
			guesses.append(guess)
	else:
		print("You didn't get it, my number was {}.".format(secret_number))
	play_agian = raw_input("Do you want to play again? ")
	if play_agian != "no":
		game()
	else:
		print("Bye!")

game()				