import random

n = random.randint(1, 100)
count = 1
guess_chances = 10
player_name = input("Hey, What's your name? ")
yes_words = ["yes", "y", "yeah", "yup", "yea", "yep"]
no_words = ["no", "nope", "nah", "not"]
print('Lovely to meet you! ' + player_name)

answer = input('Do you want to play a guessing game with me? ').lower()

if answer in no_words:
    print('Oh okay, maybe next time.')
elif answer in yes_words:
    print('Alright ' + player_name + ', I am thinking about a number between 1 and 100 and you have 10 chances to guess it...')
    print('Let’s get started!')

    while 1 <= guess_chances:
        try:
            num = int(input("Guess the number: "))
            if num > n:
                print('Your guess was too high: Guess a number lower than', num)
            elif num < n:
                print('Your guess was too low: Guess a number higher than', num)
            else:
                print('YOU WIN!')
                print('You guessed the number in ' + str(count) + ' tries!')
                break
        except ValueError:
            print("Please enter a valid number.")

        guess_chances -= 1
        print(guess_chances, 'guesses left')
        count += 1

    if guess_chances == 0:
        print("GAME OVER")
        print("The number was", n)
    print('Thanks for playing' + player_name)
else:
    print('Sorry, I didn’t get it.')
