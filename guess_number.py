import random
random_number = random.randint(1, 100)

user_name = input("Hey. What is your name? ")
number_of_guesses = 0
print('I\'m glad to meet you! {} \nLet\'s play a game with you. The idea is to think a number between 1 and 100, that you will try to guess, alright? \nDon\'t forget! You have only 3 chances so guess:'.format(user_name))

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < random_number:
        print('Your estimate is too low. Try to go up!')
    if guess > random_number:
        print('Your estimate is too high. Try to go down!')
    if guess == random_number:
        break
if guess == random_number:
    print( 'Good job {}! You guessed the number in {} tries!'.format(user_name, number_of_guesses))
else:
    print('So close, but you should have guessed the number. \n The number was {}.'.format(random_number))