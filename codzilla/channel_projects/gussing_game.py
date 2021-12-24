print('Hi, Try to guess what is my favorit android game')
print('You have five trials only, let\'s do it!!')
secret_word = 'pubg'
guess = ''
  ## or logic
guess_count = 0          # should start from zero
guess_limit = 5          # our trial number to guess it
out_of_guesses = False   # sholud be false and become True when we want stop it

while guess != secret_word:    # if it wrong 
    if guess_count < guess_limit:  # number of trial times
        guess = input('Please, enter your guess \n') 
        guess_count += 1       # how our trial rise (don't forget we inside the loop)
    else:
        out_of_guesses = True   # our loop will be stop

## we have one of this condition after loop ending
if out_of_guesses:  # it ,m ean it's True condition, we are out of guess
    print("You lose , try again")
else:
    print("woooow, you get it")