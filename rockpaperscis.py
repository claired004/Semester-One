#Claire Deng
#1/7/2025
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
ties = 0
#Function
#Main
def rpsgame():
    global wins
    global losses
    global ties
    print("""Welcome to Rock, Paper, Scissors!
        Make your move and choose between rock, paper, and scissors to play.""")
    while True:
        player = input("Please pick your move:")
        computer = random.randint(1,3)

        if computer == 1:
            competer = "Rock"
            print("The computer's move is Rock!")
        if computer == 2:
            computer = "Paper"
            print("The computer's move is Paper!")
        if computer == 3:
            computer = "Scissors"
            print("The computer's move is Scissors!")

        #Determine the outcome
        if computer == "Rock" and player.capitalize() == "Rock":
            print("You tied. The computer chose Rock. Try again.")
            ties = ties+1
        elif computer == "Rock" and player.capitalize() == "Paper":
            print("YOU WON. The computer chose Rock")
            wins = wins+1
        elif computer =="Rock" and player.capitalize() == "Scissors":
            print("Sorry, you lost. The computer chose Rock")
            losses = losses+1

        elif computer =="Paper" and player.capitalize() == "Rock":
            print("Sorry, you lost. The computer chose Paper")
            losses = losses+1
        elif computer == "Paper" and player.capitalize() == "Paper":
            print("You tied. The computer chose Paper. Try again.")
            ties = ties+1
        elif computer ==  "Paper" and player.capitalize() == "Scissors":
            print("You WON. The computer chose Paper")
            wins = wins+1

        elif computer == "Scissors" and player.capitalize() =="Rock":
            print("You WON. The computer chose Scissors")
            wins = wins+1
        elif computer == "Scissors" and player.capitalize() == "Paper":
            print("Sorry, you lost. The computer chose Scissors")
            losses = losses+1
        elif computer == "Scissors" and player.capitalize() == "Scissors":
            print("You tied. The computer chose Scissors. Try again.")
            ties = ties+1

        playagain = input("Would you like to play again?")
        if playagain.lower() == "yes":
            print("restarting.... Current scores are wins="+str(wins)+", losses="+str(losses)+", ties="+str(ties)+"!")
        else:
            print("Thank you for playing")
            break

rpsgame()



