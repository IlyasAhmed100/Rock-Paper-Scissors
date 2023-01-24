# Rock, Paper, Scissors

# Importing
from random import randint

# Introduction
welcome = "Welcome To Rock, Paper, Scissors."
width = len(welcome) + 4
widthStar = "*" * width
print(widthStar)
print("* " + welcome + " *")
print(widthStar)
# Printing Out The Rules Of The Game 
print('\n' "Here are the rules:" '\n' "1) Rock beats Scissors (Rock blunts Scissors)" '\n' "2) Paper beats Rock (Paper covers Rock)" '\n' "3) Scissors beats Paper (Scissors cuts Paper)")

# Defining Variables and Constants
PLAYER = input('\n' "Please type in your name?" + '\n')
playerScore = 0
computerScore = 0
totalGamesPlayed = 1
ROCK_WIN = "Rock blunts scissors."
PAPER_WIN = "Paper covers rock."
SCISSORS_WIN = "Scissors cut paper."
PLAYER_WIN = PLAYER + " wins this round."
COMPUTER_WIN = "Computer wins this round"

# If Player Doesn't Insert A Name
if PLAYER == " " or PLAYER == "":
    PLAYER = "Player"

# Running The Game Until A Total Of 5 Games Are Played
game = True
while game == True:
# Printing Current Rounds And Current Player And Computer Scores
    print('\n' "Round Number " + str(totalGamesPlayed))
    print("Computer current score is: " + str(computerScore))
    print(PLAYER + " current score is: " + str(playerScore))
# Getting User And Computer To Choose Rock, Paper or Scissors    
    playerChoice = input('\n' "Please choose '1' for Rock, '2' for Paper and '3' for Scissors." '\n')
    computerChoice = randint(1,3)
# Defining What The Numbers Correspond To In Terms Of Rock, Paper And Scissors
    if playerChoice == "1":
        playerChoice = "Rock"
    elif playerChoice == "2":
        playerChoice = "Paper"
    elif playerChoice == "3":
        playerChoice = "Scissors"
    else:
        print("That's not a valid input, Try Again!")

    if computerChoice == 1:
        computerChoice = "Rock"
    elif computerChoice == 2:
        computerChoice = "Paper"
    elif computerChoice == 3:
        computerChoice = "Scissors"

# Running The Game
# If The Game Is A Draw
    if playerChoice == computerChoice:
        totalGamesPlayed += 1
        print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
        print("This round is a tie, Try Again!")
# If Player Chooses Rock And Computer Chooses Paper
    elif playerChoice == "Rock":
        if computerChoice == "Paper":
            totalGamesPlayed += 1
            computerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(PAPER_WIN)
            print(COMPUTER_WIN)
# If Player Chooses Rock And Computer Chooses Scissors            
        else:
            totalGamesPlayed += 1
            playerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(ROCK_WIN)
            print(PLAYER_WIN)
# If Player Chooses Paper And Computer Chooses Scissors               
    elif playerChoice == "Paper":
        if computerChoice == "Scissors":
            totalGamesPlayed += 1
            computerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(SCISSORS_WIN)
            print(COMPUTER_WIN)
# If Player Chooses Paper And Computer Chooses Rock
        else:
            totalGamesPlayed += 1
            playerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(PAPER_WIN)
            print(PLAYER_WIN)
# If Player Chooses Scissors And Computer Chooses Rock               
    elif playerChoice == "Scissors":
        if computerChoice == "Rock":
            totalGamesPlayed += 1
            computerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(ROCK_WIN)
            print(COMPUTER_WIN)
# If Player Chooses Scissors And Computer Chooses Paper            
        else:
            totalGamesPlayed += 1
            playerScore += 1
            print(PLAYER + " chose " + playerChoice + ", computer chose " + computerChoice + ".")
            print(SCISSORS_WIN)
            print(PLAYER_WIN)

# Working Out And Printing Out The Final Score
# When It's A Draw
    if playerScore == 3 and computerScore == 3:
        print('\n' "Well done for finishing the game!" '\n' "The final score is...")
        print(PLAYER + " score = " + str(playerScore) + '\n' "Computer score = " + str(computerScore))
        print("Total number of games played was " + str(totalGamesPlayed - 1))
        print(PLAYER + " you tied with the Computer, So Close!")
        game = False
# When The Player Wins        
    elif playerScore == 3:
        print('\n' "Well done for finishing the game!" '\n' "The final score is...")
        print(PLAYER + " score = " + str(playerScore) + '\n' "Computer score = " + str(computerScore))
        print("Total number of games played was " + str(totalGamesPlayed - 1))
        print(PLAYER + " Wins, Well Done!")
        game = False
# When The Computer Wins        
    elif computerScore == 3:
        print('\n' "Well done for finishing the game!" '\n' "The final score is...")
        print(PLAYER + " score = " + str(playerScore) + '\n' "Computer score = " + str(computerScore))
        print("Total number of games played was " + str(totalGamesPlayed - 1))
        print("The Computer Wins! Unlucky, Better Luck Next Time!")
        game = False

# Asking User If He Wants To Plat Again
    while game == False:
        playAgain = input('\n' "Would you like to play again?" " Type 'y' for Yes and 'n' for No" '\n').lower()
        if playAgain == 'y':
            totalGamesPlayed = 1
            playerScore = 0
            computerScore = 0
            game = True
        elif playAgain == 'n':
            break
            
    







