
secret_number = 8
count_of_guess = 0
guess_limit = 3

while count_of_guess < guess_limit:
    guess = int(input('Guess: '))
    count_of_guess += 1
    if guess == secret_number:
        print('You Win!')
        break
else:
    print('sorry you failed')
