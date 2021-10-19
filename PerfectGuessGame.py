import random 
print("Welcome to Tushar's Game - The Perfect Guess")
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong!Guess a smaller number")
        else:
            print("You guessed it wrong!Guess a larger number")
    
print(f"You guessed the number in {guesses} guesses")
with open("highscore.txt","r") as f:
     highscore = int(f.read())
if(guesses<highscore):
    print("Woohoo! You have just broken the High Score!")
    with open("highscore.txt","w") as f:
        f.write(guesses)