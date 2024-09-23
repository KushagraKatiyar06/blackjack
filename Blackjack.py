import p1_random as p1
rng = p1.P1Random()

def menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit\n")

def statistics ():
    print(f"Number of Player wins: {myWins}")
    print(f"Number of Dealer wins: {myLoses}")
    print(f"Number of tie games: {ties}")
    print(f"Total # of games played is: {gameNumber - 1}")
    print(f"Percentage of Player wins: {winRate * 100:.1f}%\n")

gameNumber = 1
myWins = 0
myLoses = 0
ties = 0
playerExit = False

while not playerExit:
    print(f"START GAME #{gameNumber}\n")
    gameOver = False
    handValue = 0
    playerAction = 1

    while not gameOver:

        if playerAction == 1:
            cardValue = rng.next_int(13) + 1
            if cardValue == 1:
                handValue += cardValue
                print(f"Your card is a ACE!")
                print(f"Your hand is: {handValue}\n")
            elif cardValue == 11:
                cardValue = 10
                handValue += cardValue
                print(f"Your card is a JACK!")
                print(f"Your hand is: {handValue}\n")
            elif cardValue == 12:
                cardValue = 10
                handValue += cardValue
                print(f"Your card is a QUEEN!")
                print(f"Your hand is: {handValue}\n")
            elif cardValue == 13:
                cardValue = 10
                handValue += cardValue
                print(f"Your card is a KING!")
                print(f"Your hand is: {handValue}\n")
            else:
                handValue += cardValue
                print(f"Your card is a {cardValue}!")
                print(f"Your hand is: {handValue}\n")
            if handValue == 21:
                print("BLACKJACK! You win!\n")
                gameNumber += 1
                myWins += 1
                break
            elif handValue > 21:
                print("You exceeded 21! You lose.\n")
                gameNumber += 1
                myLoses += 1
                break

        elif playerAction == 2:
            dealersHand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealersHand}")
            print(f"Your hand is: {handValue}\n")

            if dealersHand > 21:
                print("You win!\n")
                gameNumber += 1
                myWins += 1
                break
            elif dealersHand == handValue:
                print("It's a tie! No one wins!\n")
                gameNumber += 1
                ties += 1
                break
            elif dealersHand < handValue:
                print("You win!\n")
                gameNumber += 1
                myWins += 1
                break
            elif dealersHand > handValue:
                print("Dealer wins!\n")
                gameNumber += 1
                myLoses += 1
                break

        elif playerAction == 3:
            if gameNumber >= 2:
                winRate = myWins / (gameNumber - 1)
            else:
                winRate = 0
            statistics()

        elif playerAction == 4:
            playerExit = True
            break

        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")

        menu()
        playerAction = int(input("Choose an option:\n"))
