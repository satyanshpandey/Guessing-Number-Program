#excercise no.3
# guessing number
n=18
guess_the_number=1
print("You have only 10 chance to guess the number:-->")
print("OK Let's Play...!")
while(guess_the_number<=10):
    guess_number=int(input("Enter the number for guess the number:--->"))
    if(guess_number>n):
        print("you entered greater number:")
    elif (guess_number<n):
        print("you guess less number")
    else:
        print("You win...!")
        print(guess_the_number,"no. of guesses took to finish")
        break
    print(10-guess_the_number,"no. of the guesses left")
    guess_the_number=guess_the_number+1