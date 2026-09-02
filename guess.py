secret_word = "ouste"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True
        break

if out_of_guesses:
    print("you are out of guesses, you lose!")
else:
    print("you win!")
