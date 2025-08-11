"""
ICS3U
Michael Sandler
Minigame ARcade
Play a variety of minigames to earn points. 
Points can be used to purchase other games, ASCII Art, or can be placed as a bet in some games.
"""

from os import system
from random import choice, randint
from time import sleep
from sys import stdout


def screen(colour1, colour2):
    """
    This function clears the screen and creates a screen for the game.

    ## Args
    colour1: str
    
    colour2: str

    ## Returns
    
    none
    """
    #clears the screen
    system('clear')
    #creates a box for the game to be played in
    print(
        colour1 +
        ''' __________________________________________________________ \n''' +
        '''|  ______________________________________________________  |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |                                                      | |\n''' +
        '''| |______________________________________________________| |\n''' +
        '''|__________________________________________________________|  ''' +
        colour2)
    return


def welcome(colour1, colour2):
    """
    This function introduces the game.
  
    ## Args
    colour1: str
    
    colour2: str
  
    ## Returns
    None
    """
    #creates welcome page for the game
    screen(colour1, colour2)
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + colour2 +
                 '-------------------------\n' + u'\u001b[18C' +
                 '|        Welcome        |\n' + u'\u001b[18C' +
                 '-------------------------\n\n' + u'\u001b[20C')
    sleep(1)
    stdout.flush()
    input('(Enter to continue)')


def numbers(points, colour1, colour2):
    """
    This function is the game about solving math problems.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str

    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    #randomly chooses question
    num1 = randint(1, 10)
    sign = choice(['+', '-', '*', '÷'])
    num2 = randint(1, 10)
    #makes sure question is solvable within the range given
    ###start of while statement###
    while num1 <= num2 or (num1 % num2) > 0:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
    ###end of while statement###
    #displays the score and the question
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + "Please solve this question:\n")
    stdout.flush()
    ans = input(u'\u001b[18C' + "{} {} {} = ".format(num1, sign, num2))
    #If teh answer isn't a number, then the score is returned without any more points.
    if ans.isdigit() == False:
        return points
    else:
        #checks if the answer is right for each sign, if the answer is correct, then 10 points are added to the score, and then the score is returned.
        if sign == '+':
            if int(ans) == num1 + num2:
                addedPoints = points + 10
                return addedPoints
            else:
                return points
        if sign == '-':
            if int(ans) == num1 - num2:
                addedPoints = points + 10
                return addedPoints
            else:
                return points
        if sign == '*':
            if int(ans) == num1 * num2:
                addedPoints = points + 10
                return addedPoints
            else:
                return points
        if sign == '÷':
            if int(ans) == num1 / num2:
                addedPoints = points + 10
                return addedPoints
            else:
                return points


def patterns(points, colour1, colour2):
    """
    This function is a game about completing a pattern
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    #sets the base pattern to be 1,2,3, and 4
    pattern = [1, 2, 3, 4]
    #chooses a number to multiply the pattern numbers
    multi = randint(2, 9)
    #chooses which number in the pattern will be missing
    space = randint(0, 3)
    ###start of for loop###
    for i in range(4):
        #multiplies the numbers in the pattern by the random number chosen
        pattern[i] = pattern[i] * multi
    ###end of for loop###
    #adds the answer to the end of the list
    pattern.append(pattern[space])
    #replaces the answer with an empty line
    pattern[space] = '_'
    #displays the score and the pattern
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + "Please solve this pattern:\n")
    stdout.flush()
    guess = input(u'\u001b[18C' + "{} {} {} {}\n".format(
        pattern[0], pattern[1], pattern[2], pattern[3]) + u'\u001b[18C')
    #checks if the input is a digit
    if guess.isdigit() == True:
        #checks if the answer is correct, if it is, then points are added to the score and the new score is returned
        if int(guess) == pattern[4]:
            addedPoints = points + 10
            return addedPoints
        else:
            return points
    else:
        return points


def memory(points, colour1, colour2):
    """
    This function is a game about remembering a given string of characters.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str

    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    string = ''
    ###start of for loop###
    for i in range(5):
        #randomly chooses the code
        string += choice(['!', '@', '#', '$', '%', '^', '&', '*'])
    ###end of for loop###
    #displays the score and the code to  remember
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + "Remember this code!!!\n" +
                 u'\u001b[18C' + "{}".format(string) + '\n' + u'\u001b[18C')
    stdout.flush()
    #gives the user time to remember the code
    sleep(3)
    #start of new screen
    screen(colour1, colour2)
    #displays the score and asks the user to input the code
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + "What was the code?\n" +
                 u'\u001b[18C')
    stdout.flush()
    #checks if the code inputeed was correct, if it is, then points are added and the new score is returned
    if input() == string:
        addedPoints = points + 10
        return addedPoints
    else:
        return points


def RockPaperScissors(points, colour1, colour2):
    """
    This function is game of rock paper Scissors that can be unlocked in the shop.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    #displays the score and explains how to select your choice
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + 'Rock Paper Scissors!\n' +
                 u'\u001b[18C' + '(r) - Rock\n' + u'\u001b[18C' +
                 '(p) - Paper\n' + u'\u001b[18C' + '(s) - Scissors\n')
    stdout.flush()
    play = input(u'\u001b[18C')
    #checks to see if the input is a number, if not, then it changes the input to be lowercase
    if play.isdigit == True:
        return points
    else:
        play.lower()
    #checks to see if the input was a valid option
    if play not in ['r', 'p', 's']:
        return addedPoints
    #computer chooses their move
    comp = choice(['r', 'p', 's'])
    #start of new screen
    screen(colour1, colour2)
    #checks the result for ties, wins, or losses
    if play == comp:
        win = -1
    elif play == 'r' and comp == 'p':
        win = 0
    elif play == 'r' and comp == 's':
        win = 1
    elif play == 'p' and comp == 'r':
        win = 1
    elif play == 'p' and comp == 's':
        win = 0
    elif play == 's' and comp == 'r':
        win = 0
    elif play == 's' and comp == 'p':
        win = 1
    #changes the string to be the choice made by the user and computer
    if play == 'r':
        play = 'Rock'
    if play == 'p':
        play = 'Paper'
    if play == 's':
        play = 'Scissors'
    if comp == 'r':
        comp = 'Rock'
    if comp == 'p':
        comp = 'Paper'
    if comp == 's':
        comp = 'Scissors'
    #displays the results and what the moves were
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n\n' + u'\u001b[20C' + 'You:    Computer:\n' +
                 u'\u001b[20C' + '{}     {}\n'.format(play, comp))
    stdout.flush()
    #if the user won, then points are added and the new score is returned
    if win == 1:
        stdout.write(u'\u001b[25C' + 'Win!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        addedPoints = points + 10
        return addedPoints
    #if the user loses, then no points are added and the score returns
    elif win == 0:
        stdout.write(u'\u001b[25C' + 'Lose!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        return addedPoints
    #if the user ties, then no points are added and the score returns
    elif win == -1:
        stdout.write(u'\u001b[25C' + 'Tie!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        return addedPoints


def coin_flip(points, colour1, colour2):
    """
    This function is game of coin flip that can be unlocked in the shop
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    #displays the score and explains the game and shows betting amounts
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + 'Coin Flip!\n' + u'\u001b[18C' +
                 "Pick an amount to bet\n" + u'\u001b[18C' +
                 "for the coin flip.\n\n" + u'\u001b[18C' +
                 '(0) - free flip\n' + u'\u001b[18C' +
                 '(50) - bet 50 points\n' + u'\u001b[18C' +
                 '(100) - bet 100 points\n' + u'\u001b[18C' +
                 '(x) - bet all your points\n')
    bet = input(u'\u001b[18C' + "Bet amount: ")
    #checks if the bet was a number or x. if the bet was a number, then that amount is bet. If the bet is x, then the bet is the total score of the user
    if bet.isdigit() == True and int(bet) in [0, 50, 100]:
        bet = int(bet)
    elif bet == 'x':
        bet = addedPoints
    else:
        #if the amount bet was invalid, then the bet is automatically set to 0
        stdout.write(u'\u001b[18C' + 'invalid amount, bet set to 0')
        bet = 0
    #if the bet is more than the score, then the bet is set to 0
    if bet > addedPoints:
        stdout.write(u'\u001b[18C' + 'bet higher than points, bet set to 0')
        bet = 0
    #asks the user whether to bet heads or tails
    choice = input('\n' + u'\u001b[18C' + "Heads or Tails?\n" + u'\u001b[18C' +
                   "H / T: ")
    #checks if the guess was a number
    if choice.isdigit() == True:
        return addedPoints
    #checks if the guess was headsd, if it was not, then it is set to tails
    if choice.lower() in ['Heads', 'heads', 'H', 'h']:
        choice = 'Heads'
    else:
        choice = 'Tails'
    #chooses a random number from 0 to 100
    flip = randint(0, 100)
    #if the number can be divided by 2, then the flip was heads, if not, then tails
    if flip % 2 == 0:
        flip = 'Heads'
    else:
        flip = 'Tails'
    #start of new screen
    screen(colour1, colour2)
    #displays the score and the result
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + 'Results: {}'.format(flip) + "\n\n" +
                 u'\u001b[20C')
    input('(Enter to continue)')
    #if the guess was right, then points are adde to the score, and the new score is returned, if not, then the amount bet is removed from the points and the new points are returned
    if choice == flip:
        addedPoints = points + bet
        if bet == 0:
            addedPoints = points + 10
        return addedPoints
    else:
        addedPoints = points - bet
        return addedPoints


def even_or_odd(points, colour1, colour2):
    """
    This function is a game where the user thinks of a number and a random number is added. If the user guessed if it will be even or odd correctly, then they get points.
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    #displays the score and explains the game
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + 'Even or Odd!\n' + u'\u001b[18C' +
                 'Two numbers are added together\n' + u'\u001b[18C' +
                 'Guess if the result is even or odd\n' + u'\u001b[18C' +
                 "Pick an amount to bet.\n\n" + u'\u001b[18C' +
                 '(0) - free play\n' + u'\u001b[18C' +
                 '(50) - bet 50 points\n' + u'\u001b[18C' +
                 '(100) - bet 100 points\n' + u'\u001b[18C' +
                 '(x) - bet all your points\n')
    stdout.flush()
    bet = input(u'\u001b[18C' + "Bet amount: ")
    #checks if the amount bet was valid
    if bet.isdigit() == True and int(bet) in [0, 50, 100]:
        bet = int(bet)
    elif bet == 'x':
        bet = addedPoints
    else:
        #if the amount bet was invalid, then the bet is set to 0
        stdout.write(u'\u001b[18C' + 'invalid amount, bet set to 0')
        bet = 0
    #checks if the amount bet is higher than the avaiable points.
    if bet > addedPoints:
        stdout.write(u'\u001b[18C' + 'bet higher than points, bet set to 0')
        bet = 0
    #asks the user if they choose even or odd
    numb = input('\n' + u'\u001b[18C' + "Even or Odd?\n" + u'\u001b[18C')
    #checks if the input was a string or not
    if numb.isdigit() == True:
        return addedPoints
    #checks if the user chose even or odd, if not then exit game
    if numb.lower() in ['Even', 'even', 'E', 'e']:
        numb = 'even'
    elif numb.lower() in ['Odd', 'odd', 'O', 'o']:
        numb = 'odd'
    else:
        return addedPoints
    #computer chooses their number
    comp = randint(1, 5)
    #user is prompted to choose their number between 1 and 5
    choice = input('\n' + u'\u001b[18C' + "Pick a number 1 - 5\n" +
                   u'\u001b[18C')
    #if the user's number is invalid, then it is set to 3 becasue 3 is the middle choice of the options
    if choice.isdigit() == False:
        stdout.write(u'\u001b[18C' + 'invalid number, number set to 3')
        choice = 3
        input('\n' + u'\u001b[18C' + "(Enter to continue)")
    elif int(choice) > 5:
        stdout.write(u'\u001b[18C' + 'invalid number, number set to 3')
        choice = 3
        input('\n' + u'\u001b[18C' + "(Enter to continue)")
    else:
        #if the number from the user is valid, then the choice is turned into a number
        choice = int(choice)
    #start of new screen
    screen(colour1, colour2)
    #checks if the added number is even, if it is then the result is set to even. If not, then the result is set to odd.
    if (comp + choice) % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    #checks if the user's guess was right. If it was, then the bet is added to the points and the updated points are returned.
    if numb == result:
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                     '\n\n' + u'\u001b[18C' +
                     'Results: {} + {} = {}\n'.format(comp, choice, comp +
                                                      choice) + u'\u001b[18C' +
                     '{}, You win!'.format(numb) + "\n\n" + u'\u001b[20C')
        input('(Enter to continue)')
        addedPoints = points + bet
        if bet == 0:
            addedPoints = points + 10
        return addedPoints
    else:
        #If the guess was wrong, then the bet is removed from the points and the updated points are returned
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                     '\n\n' + u'\u001b[18C' +
                     'Results: {} + {} = {}\n'.format(comp, choice, comp +
                                                      choice) + u'\u001b[18C' +
                     '{}, You lose'.format(numb) + "\n\n" + u'\u001b[20C')
        input('(Enter to continue)')
        addedPoints = points - bet
        return addedPoints


def blackjack(points, colour1, colour2):
    """
    This function is a game of blackjack where the player plays against the computer, whom is the dealer. The objective is to get to 21 without going over.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    #displays the score and explains the game and shows how to bet
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C' + 'Blackjack\n' + u'\u001b[18C' +
                 'Two cards are given at first\n' + u'\u001b[18C' +
                 'Get close to 21 without going over\n' + u'\u001b[18C' +
                 'Pick an amount to bet.\n\n' + u'\u001b[18C' +
                 '(0) - free play\n' + u'\u001b[18C' +
                 '(50) - bet 50 points\n' + u'\u001b[18C' +
                 '(100) - bet 100 points\n' + u'\u001b[18C' +
                 '(500) - bet 500 points\n' + u'\u001b[18C' +
                 '(x) - bet all your points\n')
    stdout.flush()
    bet = input(u'\u001b[18C' + "Bet amount: ")
    #checks if the amount bet was valid
    if bet.isdigit() == True and int(bet) in [0, 50, 100, 500]:
        bet = int(bet)
    elif bet == 'x':
        bet = addedPoints
    else:
        #if the amount bet was invalid, then the bet is set to 0
        stdout.write('\n' + u'\u001b[18C' + 'invalid amount, bet set to 0\n')
        bet = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #checks if the amount bet is higher than the avaiable points.
    if bet > addedPoints:
        stdout.write('\n' + u'\u001b[13C' +
                     'bet higher than points, bet set to 0\n')
        bet = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #all 52 cards found in a standard deck
    card = [
        'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 
        'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 
        'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥'
        ]
    #starts the result being nothing
    result = ''
    #holds the cards the player has
    playerCard = []
    #stores the cards the computer has
    compCard = []
    #sets the player's card value to 0
    sum = 0
    #sets the computer's card value to 0
    sum2 = 0
    ###start of for loop###
    for i in range(2):
        #adds cards to the player's hand
        playerCard.append(choice(card))
        #removes the added cards from the deck of cards
        card.remove(playerCard[i])
    ###end of for loop###
    ###start of for loop###
    for l in range(2):
        #adds cards to the computer's hand
        compCard.append(choice(card))
        #removes the added cards from the deck of cards
        card.remove(compCard[l])
    ###end of for loop###
    #counts the values of the cards in the computer's hand
    sum2 = cardCounter(0, compCard, playerCard)
    #counts the value o\f the cards in the user's hand
    sum = cardCounter(1, compCard, playerCard)
    #checks if the computer has gotten 21 at the start
    if sum2 == 21:
        #checks if the user has gotten the same value as the computer and decides if it a tie or a loss
        if sum != 21:
            result = 'l'
        else:
            result = 't'
    #checks if the user has gotten 21 at the start
    elif sum == 21:
        result = 'b'
    ###start of while loop###
    while result == '':
        #start of new screen
        screen(colour1, colour2)
        sum = 0
        #counts the current value of the user's cards
        sum = cardCounter(1, compCard, playerCard)
        #checks if the user has a value over 21, and if there is an A in the hand, then it is worth 1 instead of 11
        if sum > 21:
            for i in range(len(playerCard)):
                if playerCard[i] in ['A♠', 'A♣', 'A♥', 'A♦']:
                    sum -= 10
        #checks if the user has gone over the number limit
        if sum > 21:
            result = 'l'
            break
        #checks if the user has reached 21
        if sum == 21:
            result = 21
            break
        #displays one of the computer's card and all of the user's cards
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                     '\n\n' + u'\u001b[20C' + '|??| |{}|'.format(compCard[1]) +
                     u'\u001b[18C' + '\n\n\n\n\n' + u'\u001b[10C')
        for i in range(len(playerCard)):
            stdout.write(u'\u001b[2C' + '|{}|'.format(playerCard[i]))
        stdout.write('\n\n' + u'\u001b[20C' + 'Another card?\n')
        stdout.flush()
        ans = input(u'\u001b[24C' + 'Y / N\n' + u'\u001b[26C')
        #checks if the user wants another card
        if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
            #adds a card to the user's hand
            playerCard.append(choice(card))
            #removes the added cards from the deck of cards
            card.remove(playerCard[len(playerCard) - 1])
        else:
            #sets the result to the string of the value of the user's cards
            result = str(sum)
            break
    ###end of while loop###
    sum2 = 0
    #counts the value of the computer's hand
    sum2 = cardCounter(0, compCard, playerCard)
    ###start of while loop###
    #if the computer's hand is less than 17, the user hasn't lost, won, or tied, then more cards are added to the computer's hand
    while sum2 < 17 and result != 'w' and result != 'l' and result != 't':
        sum2 = 0
        #adds card to the computer's hand
        compCard.append(choice(card))
        #removes the added cards from the deck of cards
        card.remove(compCard[len(compCard) - 1])
        #counts the current value of the computer's cards
        sum2 = cardCounter(0, compCard, playerCard)
        #checks if the computer has gone over the value limit, if ther is an A in the commputer's hand, then the value of the A is 1 instead of 11
        if sum2 > 21:
            for i in range(len(compCard)):
                if compCard[i] in ['A♠', 'A♣', 'A♥', 'A♦']:
                    sum2 -= 10
    ###end of while loop###
    #checks if the result is a number, if so then the values of the user and computer are compared
    if str(result).isdigit() == True:
        if sum2 > 21:
            result = 'w'
        elif int(result) < sum2:
            result = 'l'
        elif int(result) == sum2:
            result = 't'
        else:
            result = 'w'
    #start of new screen
    screen(colour1, colour2)
    #displays the score and all the cards in both hands
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) +
                 '\n\n' + u'\u001b[18C')
    for y in range(len(compCard)):
        stdout.write(u'\u001b[2C' + '|{}|'.format(compCard[y]))
    stdout.write(u'\u001b[18C' + '\n\n\n\n\n' + u'\u001b[10C')
    for i in range(len(playerCard)):
        stdout.write(u'\u001b[2C' + '|{}|'.format(playerCard[i]))
    stdout.write('\n')
    stdout.flush()

    #if the user wins, then the bet is added to the points and the new score is returned
    if result == 'w':
        stdout.write(u'\u001b[25C' + 'Win!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        addedPoints = points + bet
        if bet == 0:
            addedPoints += 10
        return addedPoints
    #if the player bets a blackjack, then the bet multiplied by 1.5 is added to the score and returned
    if result == 'b':
        stdout.write(u'\u001b[25C' + 'Win!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        addedPoints = points + bet * 1.5
        if (addedPoints % 1) != 0:
            addedPoints += .5
        if bet == 0:
            addedPoints += 15
        addedPoints = int(addedPoints)
        return addedPoints
    #if the user loses, then no points are added and the score returns
    elif result == 'l':
        stdout.write(u'\u001b[25C' + 'Lose!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        addedPoints -= bet
        return addedPoints
    #if the user ties, then no points are added and the score returns
    elif result == 't':
        stdout.write(u'\u001b[25C' + 'Tie!' + "\n\n" + u'\u001b[20C')
        stdout.flush()
        input('(Enter to continue)')
        return addedPoints


def cardCounter(hand, compCard, playerCard):
    """
    This function counts the value of the cards dealt to the user or computer.
  
    ## Args
    hand: int
    
    compCard: list
    
    playerCard: list

    ## Returns
    value: int
    """
    value = 0
    #checks if the hand being counted is the computer's or the player's
    if hand == 0:
        ###start of for loop###
        for m in range(len(compCard)):
            #adds the value of the number on the card
            if '2' in compCard[m]:
                value += 2
            elif '3' in compCard[m]:
                value += 3
            elif '4' in compCard[m]:
                value += 4
            elif '5' in compCard[m]:
                value += 5
            elif '6' in compCard[m]:
                value += 6
            elif '7' in compCard[m]:
                value += 7
            elif '8' in compCard[m]:
                value += 8
            elif '9' in compCard[m]:
                value += 9
            elif '10' in compCard[m]:
                value += 10
                #adds 11 for the value of A
            elif compCard[m] in ['A♠', 'A♣', 'A♥', 'A♦']:
                value += 11
            else:
                #adds 10 for the value of the face cards
                value += 10
        ###end of for loop###
    elif hand == 1:
        ###start of for loop###
        for m in range(len(playerCard)):
            #adds the value of the number on the card
            if '2' in playerCard[m]:
                value += 2
            elif '3' in playerCard[m]:
                value += 3
            elif '4' in playerCard[m]:
                value += 4
            elif '5' in playerCard[m]:
                value += 5
            elif '6' in playerCard[m]:
                value += 6
            elif '7' in playerCard[m]:
                value += 7
            elif '8' in playerCard[m]:
                value += 8
            elif '9' in playerCard[m]:
                value += 9
            elif '10' in playerCard[m]:
                value += 10
                #adds 11 for the value of A
            elif playerCard[m] in ['A♠', 'A♣', 'A♥', 'A♦']:
                value += 11
            else:
                #adds 10 for the value of the face cards
                value += 10
        ###end of for loop###
    return value

def dice(points, colour1, colour2):
    """
    This function is a game where the player rolls dice to get a specific number.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    dice=[0,0]
    part = 'roll'
    point = 0
    #displays the score and explains the game and shows how to bet
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) + '\n\n' + 
                 u'\u001b[18C' + 'Dice\n' + 
                 u'\u001b[8C' + 'Two dice are rolled, if you choose a pass bet \n' + 
                 u'\u001b[8C' + 'try to get 7 or 11 without rolling 2, 3, or 12,\n' + 
                 u'\u001b[8C' + 'or roll the same number twice before rolling a 7 \n' + 
                 u'\u001b[8C' + 'if you choose a don\'t pass bet,\n' + 
                 u'\u001b[8C' + 'the opposite is true and 12 is a tie \n\n' + 
                 u'\u001b[18C' + 'Pick an amount to bet.\n' + 
                 u'\u001b[18C' + '(0) - free play\n' + 
                 u'\u001b[18C' + '(50) - bet 50 points\n' + 
                 u'\u001b[18C' + '(100) - bet 100 points\n' + 
                 u'\u001b[18C' + '(x) - bet all your points\n')
    stdout.flush()
    bet = input(u'\u001b[18C' + "Bet amount: ")
    #checks if the amount bet was valid
    if bet.isdigit() == True and int(bet) in [0, 50, 100]:
        bet = int(bet)
    elif bet == 'x':
        bet = addedPoints
    else:
        #if the amount bet was invalid, then the bet is set to 0
        stdout.write('\n' + u'\u001b[18C' + 'invalid amount, bet set to 0\n')
        bet = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #checks if the amount bet is higher than the avaiable points.
    if bet > addedPoints:
        stdout.write('\n' + u'\u001b[13C' +
                     'bet higher than points, bet set to 0\n')
        bet = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #start of new screen
    screen(colour1, colour2)
    #shows the two game types and asks the user to choose one
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n')
    play = input(u'\u001b[23C' + "Game Type:\n"+u'\u001b[18C' + "Pass or Don't Pass: ")
    #check what game type the user chose
    if play.lower() in ["don't pass", 'dont pass', "don'tpass", 'dontpass',"don't", 'dont']:
        play = "don't"
    elif play.lower() in ['pass','pass line']:
        play = 'pass'
    else:
        #sets the game type to pass if th euser doesn't choose one of the options
        play = 'pass'
        stdout.write(u'\u001b[13C' + "Unknown Game Type, Game Type set to Pass\n")
        input(u'\u001b[20C'+'(Enter to continue)')
    ###start of for loop###
    #rolls the dice to get the first number
    for i in range(2):
        dice[i]=randint(1,6)
    ###end of for loop###
    #checks if the total of the roll is one of the numbers that ends the game
    if (dice[0]+dice[1]) in [2,3,7,11,12]:
        part = 'end'
    else:
        point = (dice[0]+dice[1])
    while part == 'roll':
        #start of new screen
        screen(colour1, colour2)
        #shows the dice after they have been rolled
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n\n' + 
                     u'\u001b[18C' + "Point:" + str(point)+'\n' +
                     u'\u001b[18C' + "    ___          ___        \n" +
                     u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                     u'\u001b[18C' + "   |___|        |___|       \n" 
                    )
        #asks the user to roll again.
        input(u'\u001b[20C'+'(Enter to roll again)')
        ###start of for loop###
        #rolls the dice
        for i in range(2):
            dice[i]=randint(1,6)
        ###end of for loop###
        #checks if the number rolled is the original number or 7.
        if (dice[0]+dice[1]) in [point, 7]:
            part = 'end'
    if part == 'end':
        #checks if the number rolled was on the first roll
        if point == 0:
            #checks the game type
            if play == 'pass':
                #checks if the number rolled is 7 or 11 and then rewards points
                if (dice[0]+dice[1]) in [7,11]:
                    stdout.write(u'\u001b[25C' + 'Win!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints = points + bet
                    if bet == 0:
                        addedPoints += 10
                    return addedPoints
                #checks if any of the numbers were losing numbers and then removes points
                elif (dice[0]+dice[1]) in [2,3,12]:
                    stdout.write(u'\u001b[25C' + 'Lose!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints -= bet
                    return addedPoints
            #check the game type
            elif play == "don't":
                #checks if the nubers rolled are wining numbers and then rewards points
                if (dice[0]+dice[1]) in [2,3]:
                    stdout.write(u'\u001b[25C' + 'Win!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints = points + bet
                    if bet == 0:
                        addedPoints += 10
                    return addedPoints
                #checks if the numbers rolled were losing numbers and removes points
                elif (dice[0]+dice[1]) in [7,11]:
                    stdout.write(u'\u001b[25C' + 'Lose!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints -= bet
                    return addedPoints
                #checks if the number rolled is 12, if so then te game is a tie
                elif (dice[0]+dice[1]) == 12:
                    stdout.write(u'\u001b[25C' + 'Tie!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    return addedPoints
        else:
            #checks the game type
            if play == 'pass':
                #if the same number was rolled twice, points are added
                if (dice[0]+dice[1]) == point:
                    #start of new screen
                    screen(colour1, colour2)
                    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n\n' + 
                                 u'\u001b[25C' + 'Win!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints = points + bet
                    if bet == 0:
                        addedPoints += 10
                    return addedPoints
                #if a 7 was rolled before the original number, removes points
                elif (dice[0]+dice[1]) == 7:
                    #start of new screen
                    screen(colour1, colour2)
                    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n\n' +
                                 u'\u001b[25C' + 'Lose!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints -= bet
                    return addedPoints
            #checks the game type
            elif play == "don't":
                #checks if the number rolled was 7, if so then returns points
                if (dice[0]+dice[1]) == 7:
                    #start of new screen
                    screen(colour1, colour2)
                    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n\n' +
                                 u'\u001b[25C' + 'Win!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints = points + bet
                    if bet == 0:
                        addedPoints += 10
                    return addedPoints
                #checks if the same nuber was rolled tiwce, and removes points
                elif (dice[0]+dice[1]) == point:
                    #start of new screen
                    screen(colour1, colour2)
                    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n\n' +
                                 u'\u001b[25C' + 'Lose!\n\n' +
                                 u'\u001b[18C' + "    ___          ___        \n" +
                                 u'\u001b[18C' + "   | {} |        | {} |        \n".format(dice[0],dice[1]) +
                                 u'\u001b[18C' + "   |___|        |___|       \n"
                                )
                    stdout.flush()
                    input(u'\u001b[20C'+'(Enter to continue)')
                    addedPoints -= bet
                    return addedPoints 

def roulette(points, colour1, colour2):
    """
    This function is a game where the player places a bet for a roulette wheel.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #start of new screen
    screen(colour1, colour2)
    addedPoints = points
    #introduces win variable
    win = '?'
    #sets what number are on the wheel
    wheel = ['0','00','1','2','3','4','5','6','7','8','9','10','11','12',
             '13','14','15','16','17','18','19','20','21','22','23','24',
             '25','26','27','28','29','30','31','32','33','34','35','36']
    #displays the score and explains the game and shows how to bet
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points) + '\n\n' + 
                 u'\u001b[18C' + 'Roulette\n' + 
                 u'\u001b[18C' + 'This is a simplified Roulette.\n' + 
                 u'\u001b[18C' + 'Pick a betting option and \n' + 
                 u'\u001b[18C' + 'then spin the wheel to see if you win\n' + 
                 u'\u001b[18C' + 'Pick an amount to bet.\n' + 
                 u'\u001b[18C' + '(0) - free play\n' + 
                 u'\u001b[18C' + '(50) - bet 50 points\n' + 
                 u'\u001b[18C' + '(100) - bet 100 points\n' + 
                 u'\u001b[18C' + '(x) - bet all your points\n')
    stdout.flush()
    amount = input(u'\u001b[18C' + "Bet amount: ")
    #checks if the amount bet was valid
    if amount.isdigit() == True and int(amount) in [0, 50, 100]:
        amount = int(amount)
    elif amount == 'x':
        amount = addedPoints
    else:
        #if the amount bet was invalid, then the bet is set to 0
        stdout.write('\n' + u'\u001b[18C' + 'invalid amount, bet set to 0\n')
        amount = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #checks if the amount bet is higher than the avaiable points.
    if amount > addedPoints:
        stdout.write('\n' + u'\u001b[13C' +
                     'bet higher than points, bet set to 0\n')
        amount = 0
        stdout.write(u'\u001b[20C')
        input('(Enter to continue)')
    #start of new screen
    screen(colour1, colour2)
    #displayes roulette table, the colour of specific numbers, and what the return is on the specified bets
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n' +
                 u'\u001b[4C' + '                                  / \ /  \      \n' +
                 u'\u001b[4C' + '  Single bet            _________|' + green + ' 0 ' + colour2 + '| ' + green + '00' + colour2 + ' |     \n' +
                 u'\u001b[4C' + '     30:1              |1-18 |   | ' + red + '1' + colour2 + '| ' + grey + '2' + colour2 + '| ' + red + '3' + colour2 + '|     \n' +
                 u'\u001b[4C' + '  Dozen bet            |-----|1st| ' + grey + '4' + colour2 + '| ' + red + '5' + colour2 + '| ' + grey + '6' + colour2 + '|     \n' +
                 u'\u001b[4C' + '  or Column bet        |Even |12 | ' + red + '7' + colour2 + '| ' + grey + '8' + colour2 + '| ' + red + '9' + colour2 + '|     \n' +
                 u'\u001b[4C' + '     2:1               |-----|___|' + grey + '10' + colour2 + '|' + grey + '11' + colour2 + '|' + red + '12' + colour2 + '|     \n' +
                 u'\u001b[4C' + '  Even or Odd          | ' + red + 'Red' + colour2 + ' |   |' + grey + '13' + colour2 + '|' + red + '14' + colour2 + '|' + grey + '15' + colour2 + '|     \n' +
                 u'\u001b[4C' + '  or ' + red + 'Red' + colour2 + ' or ' + grey + 'Black' + colour2 + '      |-----|2nd|' + red + '16' + colour2 + '|' + grey + '17' + colour2 + '|' + red + '18' + colour2 + '|     \n' +
                 u'\u001b[4C' + '  or 1-18 or 19-36     |' + grey + 'Black' + colour2 + '|12 |' + red + '19' + colour2 + '|' + grey + '20' + colour2 + '|' + red + '21' + colour2 + '|     \n' +
                 u'\u001b[4C' + '     1:1               |-----|___|' + grey + '22' + colour2 + '|' + red + '23' + colour2 + '|' + grey + '24' + colour2 + '|     \n' +
                 u'\u001b[4C' + '                       | Odd |   |' + red + '25' + colour2 + '|' + grey + '26' + colour2 + '|' + red + '27' + colour2 + '|     \n' +
                 u'\u001b[4C' + '                       |-----|3rd|' + grey + '28' + colour2 + '|' + grey + '29' + colour2 + '|' + red + '30' + colour2 + '|     \n' +
                 u'\u001b[4C' + '                       |19-36|12 |' + grey + '31' + colour2 + '|' + red + '32' + colour2 + '|' + grey + '33' + colour2 + '|     \n' +
                 u'\u001b[4C' + '                       |_____|___|' + red + '34' + colour2 + '|' + grey + '35' + colour2 + '|' + red + '36' + colour2 + '|     \n' +
                 u'\u001b[4C' + '                                 |C1|C2|C3|     \n'+
                 u'\u001b[4C' + '                                 |__|__|__|     \n' )
    #asks the user what bet they would like to make
    bet = input(u'\u001b[1A' + u'\u001b[6C' + 'Bet option: ').lower()
    #checks which bet type was selected and sets the bet to a specific variable.
    if bet in ['red','r']:
        bet = 'r'
    elif bet in ['black','b']:
        bet = 'b'
    elif bet in ['even','e']:
        bet = 'even'
    elif bet in ['odd','o']:
        bet = 'odd'
    elif bet in ['1-18']:
        bet = '1-18'
    elif bet in ['19-36']:
        bet = '19-36'
    elif bet in ['1st 12','1st dozen','1st12','1stdozen','1 12','1 dozen','112','1dozen']:
        bet = '1st 12'
    elif bet in ['2nd 12','2nd dozen','2nd12','2nddozen','2 12','2 dozen','212','2dozen']:
        bet = '2nd 12'
    elif bet in ['3rd 12','3rd dozen','3rd12','3rddozen','3 12','3 dozen','312','3dozen']:
        bet = '3rd 12'
    elif bet in ['column 1','1st column','column1','1stcolumn','c 1','1 column','c1','1column']:
        bet = '1st column'
    elif bet in ['column 2','2nd column','column2','2ndcolumn','c 2','2 column','c2','2column']:
        bet = '2nd column'
    elif bet in ['column 3','3rd column','column3','3rdcolumn','c 3','3 column','c3','3column']:
        bet = '3rd column'
    elif bet.isdigit() == True and bet in wheel:
        bet = str(bet)
    else:
        #returns the points if the bet inputed was not one of the bets specified
        #start of new screen
        screen(colour1, colour2)
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n' +
                     u'\u001b[18C' + 'Invalid bet, Points are returned\n')
        input(u'\u001b[18C' + '(Enter to continue)')
        return addedPoints
    #spins the roulette wheel
    spin = choice(wheel)
    #start of new screen
    screen(colour1, colour2)
    #displayes the score and what the result was from spinning the wheel
    stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(points)+'\n' +
                 u'\u001b[18C' + 'spin: {}\n'.format(spin))
    #checks what the bet type was
    if bet.isdigit() == True:
        #checks if the user won and adds points
        if bet == spin:
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount)*30)))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)*30
            return addedPoints
        else:
            #removes points if the user lost
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points - int(amount)
            return addedPoints
    elif bet in ['1st column','2nd column','3rd column']:
        #checks if the bet chosen won and adds points
        if bet == '1st column' and spin in ['1','4','7','10','13','16','19','22','25','28','31','34']:
            win = True
        elif bet == '2nd column' and spin in ['2','5','8','11','14','17','20','23','26','29','32','35']:
            win = True
        elif bet == '3rd column' and spin in ['3','6','9','12','15','18','21','24','27','30','33','36']:
            win = True
        else:
            win = False
        if win == True:            
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount)*2)))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)*2
            return addedPoints
        else:
            #if the bet lost, removes points
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points-int(amount)
            return addedPoints
    elif bet in ['1st 12','2nd 12','3rd 12']:
        #checks if the bet selected won, and adds points
        if bet == '1st 12' and spin in ['1','2','3','4','5','6','7','8','9','10','11','12']:
            win = True
        elif bet == '2nd 12' and spin in ['13','14','15','16','17','18','19','20','21','22','23','24']:
            win = True
        elif bet == '3rd 12' and spin in ['25','26','27','28','29','30','31','32','33','34','35','36']:
            win = True
        else:
            win = False
        if win == True:            
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount)*2)))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)*2
            return addedPoints
        else:
            #removes points if the bet lost
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points-int(amount)
            return addedPoints
    elif bet in ['1-18','19-36']:
        #checks if the bet selected won and adds points
        if bet == '1-18' and spin in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']:
            win = True
        elif bet == '19-36' and spin in ['19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']:
            win = True
        else:
            win = False
        if win == True:
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount))))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)
            return addedPoints
        else:
            #removes points if the bet lost
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points-int(amount)
            return addedPoints
    elif bet in ['even','odd']:
        #check if the bet selected won and adds points
        if bet == 'even' and (int(spin)%2) == 0 and spin not in ['0','00']:
            win = True
        elif bet == 'odd' and (int(spin)%2) == 1 and spin not in ['0','00']:
            win = True
        else:
            win = False
        if win == True:
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount))))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)
            return addedPoints
        else:
            #removes points if the bet lost
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points-int(amount)
            return addedPoints
    elif bet in ['r','b']:
        #checks if the selected bet won and adds points
        if bet == 'r' and spin in ['1','3','5','7','9','12','14','16','18','19','21','23','25','27','30','32','34','36']:
            win = True
        elif bet == 'b' and spin in ['2','4','6','8','10','11','13','15','17','20','22','24','26','28','29','31','33','35']:
            win = True
        else:
            win = False
        if win == True:
            if amount == 0:
                amount = 10
            stdout.write('\n' + u'\u001b[18C' + 'You win!\n' +
                        u'\u001b[18C' + 'Your winings: {}\n'.format((int(amount))))
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points + int(amount)
            return addedPoints
        else:
            #removes points if teh bet lost
            stdout.write('\n' + u'\u001b[18C' + 'You Lose!\n\n')
            input(u'\u001b[14C' + '(Enter to continue)')
            addedPoints = points-int(amount)
            return addedPoints    

def spin(points, colour1, colour2):
    """
    This function is a game where the player spins a slot machine.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str
    
    ## Returns
    addedPoints: int
    """
    #introduces play variable
    play = ''
    addedPoints = points
    #defines what the different options are for spinning
    spin = ['⅓','∑','∞','⇄','♪','7']
    #sets the initial values to be ?
    slot = ['?','?','?']
    ###start of while loop###
    #the game loops until the player exits or runs out of points
    while play !='e':
        #start of new screen
        screen(colour1, colour2)
        #displays the screen of the machine and the returns for getting specific values
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(addedPoints) + '\n\n' + 
                     u'\u001b[18C' + 'Slot Machine\n' + 
                     u'\u001b[8C' + ' ___________________________________________ \n' + 
                     u'\u001b[8C' + '| _________________________________________ |\n' + 
                     u'\u001b[8C' + '| |                       | ⅓      X 1    | |\n' + 
                     u'\u001b[8C' + '| |                       | ⅓ ⅓    X 2    | |\n' + 
                     u'\u001b[8C' + '| |  {}     {}     {}        | ⅓ ⅓ ⅓  X 3    | |\n'.format(slot[0],slot[1],slot[2]) + 
                     u'\u001b[8C' + '| |                       | ∑ ∑ ∑  X 5    | |\n' + 
                     u'\u001b[8C' + '| |                       | ∞ ∞ ∞  X 10   | |\n' + 
                     u'\u001b[8C' + '| |                       | ⇄ ⇄ ⇄  X 20   | |\n' + 
                     u'\u001b[8C' + '| |                       | ♪ ♪ ♪  X 50   | |\n' + 
                     u'\u001b[8C' + '| |                       | 7 7 7  X 100  | |\n' + 
                     u'\u001b[8C' + '| |_______________________|_______________| |\n' +  
                     u'\u001b[8C' + '|___________________________________________|\n' + 
                     u'\u001b[8C' + '(y) - spin    (e) - exit.\n')
        stdout.flush()
        #asks the user if they want to spin
        play = input(u'\u001b[18C' + "5 points to spin?: ").lower()
        #checks if the player wants to play and if they have enough points
        if play in ['y','yes','ye'] and addedPoints>=5:
            play = 'y'
        else:
            #if the player doesn't have enough points or doesn't want to play, they exit
            play = 'e'
        if play == 'y':
            ##start of for loop##
            for i in range(3):
                #selects the result of the spin
                slot[i] = choice(spin)
            ##end of for loop##
            ##start of for loop##
            for i in range(0,randint(1,10)):
            ##end of for loop##
                #start of new screen
                screen(colour1, colour2) 
                #shows that the machine is spinning
                stdout.write(u'\u001b[20A' + u'\u001b[18C' + "score:" + str(addedPoints) + '\n\n' + 
                             u'\u001b[18C' + 'Slot Machine\n' + 
                             u'\u001b[8C' + ' ___________________________________________ \n' + 
                             u'\u001b[8C' + '| _________________________________________ |\n' + 
                             u'\u001b[8C' + '| |                       | ⅓      X 1    | |\n' + 
                             u'\u001b[8C' + '| |                       | ⅓ ⅓    X 2    | |\n' + 
                             u'\u001b[8C' + '| |  {}     {}     {}        | ⅓ ⅓ ⅓  X 3    | |\n'.format(choice(spin),choice(spin),choice(spin)) +
                             u'\u001b[8C' + '| |                       | ∑ ∑ ∑  X 5    | |\n' + 
                             u'\u001b[8C' + '| |                       | ∞ ∞ ∞  X 10   | |\n' + 
                             u'\u001b[8C' + '| |                       | ⇄ ⇄ ⇄  X 20   | |\n' + 
                             u'\u001b[8C' + '| |                       | ♪ ♪ ♪  X 50   | |\n' + 
                             u'\u001b[8C' + '| |                       | 7 7 7  X 100  | |\n' + 
                             u'\u001b[8C' + '| |_______________________|_______________| |\n' +  
                             u'\u001b[8C' + '|___________________________________________|\n' + 
                             u'\u001b[8C' + 'spin the machine to get points.\n')
                sleep(.25)
            #determines if the result is a winning pattern 
            if '⅓' in slot:
                addedPoints +=5
            elif '⅓' in slot and slot[0] == slot[1] or slot[0] == slot[2] or slot[1] == slot[2]:
                addedPoints +=10
            elif slot[0]==slot[1] and slot[1]==slot[2]:
                if '⅓' in slot:
                    addedPoints+=15
                elif '∑' in slot:
                    addedPoints+=25
                elif '∞' in slot:
                    addedPoints+=50
                elif '⇄' in slot:
                    addedPoints+=100
                elif '♪' in slot:
                    addedPoints+=250
                elif '7' in slot:
                    addedPoints+=500
            else:
                #if the pattern does not give any points, 5 points are removed
                addedPoints-=5
    else:
        #returns the current points of the player
        return addedPoints
    ###end of while loop###
def store(points, colour1, colour2):
    """
    This function represents a store that items can bought from.
  
    ## Args
    points: int
    
    colour1: str
    
    colour2: str

    ## Returns
    addedPoints: int
    """
    buy = ''
    addedPoints = points
    while buy !='e':
        #start of new screen
        screen(colour1, colour2)
        #displays the score
        stdout.write(u'\u001b[21A' + u'\u001b[18C' + "score:" + str(addedPoints) + '\n')
        ###start of for loop###
        for i in range(len(artOptions)):
            #prints the different ASCII art that can be purchased
            stdout.write(u'\u001b[18C' +
                         '({}) - {} - 50\n'.format(i, artOptions[i]))
        ###end of for loop###
        buy = ''
        #displays the different games that can be unlocked with points if they were not already purchased
        if 4 not in games:
            stdout.write(u'\u001b[18C' + '(p) - Rock Paper Scissors - 50\n')
        if 5 not in games:
            stdout.write(u'\u001b[18C' + '(c) - Coin Flip - 100\n')
        if 6 not in games:
            stdout.write(u'\u001b[18C' + '(o) - Even or Odd - 100\n')
        if 7 not in games:
            stdout.write(u'\u001b[18C' + '(j) - Blackjack - 100\n')
        if 8 not in games:
            stdout.write(u'\u001b[18C' + '(d) - Dice - 100\n')
        if 9 not in games:
            stdout.write(u'\u001b[18C' + '(l) - Roulette - 100\n')  
        if 10 not in games:
            stdout.write(u'\u001b[18C' + '(s) - Slot Machine - 100\n')    
        #displays what colours can be bought if they are not already purchased
        if 'red' not in colourOptions:
            stdout.write(u'\u001b[18C' + '(r) - add red - 50\n')
        if 'yellow' not in colourOptions:
            stdout.write(u'\u001b[18C' + '(y) - add yellow - 50\n')
        if 'grey' not in colourOptions:
            stdout.write(u'\u001b[18C' + '(g) - add grey - 50\n')
        if 'blue' not in colourOptions:
            stdout.write(u'\u001b[18C' + '(b) - add blue - 50\n')
        if 'blue' not in colourOptions:
            stdout.write(u'\u001b[18C' + '(t) - add turquoise - 50\n')
    
        buy = input(u'\u001b[18C' + '(e to exit): ')
        #checks if the user's choice was a number to purchase ASCII art
        if buy.isdigit() == True:
            #checks if the user has enough money and if the number was in range of the index
            if int(buy) <= len(artOptions) - 1 and points >= 50:
                #adds the art to the list of bought art and removes the art from the store as an option
                art.append(artOptions[int(buy)])
                del artOptions[int(buy)]
                #removes the amount of points needed
                addedPoints -= 50
        #checks if the input was for the games that can be purchased and if there are enough points to buy them. When bought, the list of games is updated with the game bought an removes the amount of points needed to unlock them.
        if buy.lower() == 'p' and addedPoints >= 50 and 4 not in games:
            games.append(4)
            addedPoints -= 50
        if buy.lower() == 'c' and addedPoints >= 100 and 5 not in games:
            games.append(5)
            addedPoints -= 100
        if buy.lower() == 'o' and addedPoints >= 100 and 6 not in games:
            games.append(6)
            addedPoints -= 100
        if buy.lower() == 'j' and addedPoints >= 100 and 7 not in games:
            games.append(7)
            addedPoints -= 100
        if buy.lower() == 'd' and addedPoints >= 100 and 8 not in games:
            games.append(8)
            addedPoints -= 100
        if buy.lower() == 'l' and addedPoints >= 100 and 9 not in games:
            games.append(9)
            addedPoints -= 100
        if buy.lower() == 's' and addedPoints >= 100 and 10 not in games:
            games.append(10)
            addedPoints -= 100
        #checks if the user has enough points to purchase the selected colour. If there are enough points, the points are removed, the colour is added to the list, and the selected colour is removed from the store.
        if buy.lower() == 'r' and addedPoints >= 50:
            colourOptions.append('red')
            addedPoints -= 50
        if buy.lower() == 'y' and addedPoints >= 50:
            colourOptions.append('yellow')
            addedPoints -= 50
        if buy.lower() == 'g' and addedPoints >= 50:
            colourOptions.append('grey')
            addedPoints -= 50
        if buy.lower() == 'b' and addedPoints >= 50:
            colourOptions.append('blue')
            addedPoints -= 50
        if buy.lower() == 't' and addedPoints >= 50:
            colourOptions.append('turquoise')
            addedPoints -= 50
    else:
        #returns points when finished
        return addedPoints


def artwork(colour1, colour2):
    """
    This function prints the selected artwork that was purchased.
  
    ## Args
    colour1: str
    
    colour2: str

    ## Returns
    nothing
    """
    option = ''
    ###start of while loop###
    while option != 'e':
        #start of new screen
        screen(colour1, colour2)
        stdout.write(u'\u001b[20A')
        ##start of for loop##
        for i in range(len(art)):
            #displays the purchased art
            stdout.write(u'\u001b[18C' + '({}) - {}\n'.format(i, art[i]))
        ##end of for loop##
        #displays how to exit
        stdout.write(u'\u001b[18C' + "(e) - Exit\n" + u'\u001b[18C')
        stdout.flush()
        option = input()
        #checks if the input was valid. If it is not, then nothing happens. If it is, then it will display the coresponding ASCII art.
        if option.isdigit() == False:
            ''
        elif option.isdigit() and int(option) >= len(art):
            ''
        elif option.isdigit() == True and int(option) <= len(art):
            if art[int(option)] == 'Tree':
                #start of new screen
                screen(colour1, colour2)
                #displays custom ASCII art
                stdout.write(
                    u'\u001b[20A' + u'\u001b[4C' + green +
                    '                       __-__                   \n' +
                    u'\u001b[4C' +
                    '                    /~-     ~~\                      \n' +
                    u'\u001b[4C' + '                /~-~ ' + red + '()' +
                    green + '  `  `  -~~\  \n' + u'\u001b[4C' +
                    '             /~~             ' + red + '()' + green +
                    '    ~~\ \n' + u'\u001b[4C' + '           {  `  ' + red +
                    '()' + green + '  `   ' + red + '()' + green +
                    '   `    `   } \n' + u'\u001b[4C' +
                    '            \   _      ' + red + '()' + green +
                    '  ` _    `   / \n' + u'\u001b[4C' +
                    '              \~~~ ' + brown + '| |' + green + '~_-~_' +
                    brown + '|| //' + green + ' ~~~/ \n' + u'\u001b[4C' +
                    brown +
                    '                   | |     ||//                \n' +
                    u'\u001b[4C' +
                    '                   \ \    / /                        \n' +
                    u'\u001b[4C' +
                    '                    \  \_/ |                         \n' +
                    u'\u001b[4C' +
                    '                     |     |                         \n' +
                    u'\u001b[4C' +
                    '                     |     |                         \n' +
                    u'\u001b[4C' +
                    '                     |     |                         \n' +
                    u'\u001b[4C' +
                    '                     |     |                         \n' +
                    u'\u001b[4C' +
                    '                    /       \                        \n' +
                    u'\u001b[4C' +
                    '              ___=--         --=___                  \n' +
                    colour2)
                input(u'\u001b[20C' + "(Enter to Continue)")
            elif art[int(option)] == 'Cactus':
                #start of new screen
                screen(colour1, colour2)
                #displays custom ASCII art
                stdout.write(
                    u'\u001b[20A' + u'\u001b[4C' + green +
                    '                                          \n' +
                    u'\u001b[4C' +
                    '                                                \n' +
                    u'\u001b[4C' +
                    '                                                \n' +
                    u'\u001b[4C' +
                    '                      /||\                      \n' +
                    u'\u001b[4C' +
                    '                      |||| /|\                  \n' +
                    u'\u001b[4C' +
                    '                  /|\ |||| |||                  \n' +
                    u'\u001b[4C' +
                    '                  ||| |||| |||                  \n' +
                    u'\u001b[4C' +
                    '                  ||| |||||||/                  \n' +
                    u'\u001b[4C' +
                    '                  \|||||||~~\'                  \n' +
                    u'\u001b[4C' +
                    '                   `~~||||                      \n' +
                    u'\u001b[4C' +
                    '                      ||||                      \n' +
                    u'\u001b[4C' +
                    '                      ||||                      \n' +
                    u'\u001b[4C' +
                    '                      ||||                      \n' +
                    u'\u001b[4C' +
                    '                      ||||                      \n' +
                    u'\u001b[4C' + yellow + '.*,_,.-*._.*,.,.,-__.,' + green +
                    '||||' + yellow + ',..*._.*,.,.,-__.,.,.*._,.\n' + colour2)
                input(u'\u001b[20C' + "(Enter to Continue)")

            elif art[int(option)] == 'Game System':
                #start of new screen
                screen(colour1, colour2)
                #displays custom ASCII art
                stdout.write(
                    u'\u001b[22A' + u'\u001b[4C' + colour2 +
                    ' __________________________________________________ \n' +
                    u'\u001b[4C' +
                    '|  ______________________________________________  |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' + '| |            ' + colour1 +
                    '-------------------------' + colour2 + '         | |\n' +
                    u'\u001b[4C' + '| |            ' + colour1 +
                    '|        Welcome        |' + colour2 + '         | |\n' +
                    u'\u001b[4C' + '| |            ' + colour1 +
                    '-------------------------' + colour2 + '         | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' + '| |              ' + colour1 +
                    '(Enter to continue)' + colour2 + '             | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |                                              | |\n' +
                    u'\u001b[4C' +
                    '| |______________________________________________| |\n' +
                    u'\u001b[4C' +
                    '|__________________________________________________|\n' +
                    colour2)
                input(u'\u001b[20C' + "(Enter to Continue)")
            elif art[int(option)] == 'Chrome Logo':
                #start of new screen
                screen(colour1, colour2)
                #displays custom ASCII art
                stdout.write(
                    u'\u001b[21A' + red + u'\u001b[12C' +
                    '            ▓▓▓▓▓▓▓▓▓▓▓           \n' + u'\u001b[12C' +
                    '        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        \n' + u'\u001b[12C' +
                    '     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     \n' + u'\u001b[12C' +
                    '    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    \n' + green +
                    u'\u001b[12C' + '  ▓▓' + red +
                    '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  \n' + green +
                    u'\u001b[12C' + '  ▓▓▓▓' + red +
                    '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  \n' + green + u'\u001b[12C' +
                    '▓▓▓▓▓▓' + red + '▓▓▓▓▓▓▓▓' + white + '▓▓▓▓▓▓' + yellow +
                    '▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n' + green + u'\u001b[12C' + '▓▓▓▓▓▓▓▓' +
                    red + '▓▓▓▓' + white + '▓▓' + blue + '▓▓▓▓▓▓' + white +
                    '▓▓' + yellow + '▓▓▓▓▓▓▓▓▓▓▓▓\n' + green + u'\u001b[12C' +
                    '▓▓▓▓▓▓▓▓▓▓' + red + '▓▓' + white + '▓▓' + blue +
                    '▓▓▓▓▓▓' + white + '▓▓' + yellow + '▓▓▓▓▓▓▓▓▓▓▓▓\n' +
                    green + u'\u001b[12C' + '▓▓▓▓▓▓▓▓▓▓▓▓' + white + '▓▓' +
                    blue + '▓▓▓▓▓▓' + white + '▓▓' + yellow +
                    '▓▓▓▓▓▓▓▓▓▓▓▓\n' + green + u'\u001b[12C' +
                    '▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + white + '▓▓▓▓▓▓' + green + '▓▓' +
                    yellow + '▓▓▓▓▓▓▓▓▓▓▓▓\n' + green + u'\u001b[12C' +
                    '  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + yellow + '▓▓▓▓▓▓▓▓▓▓  \n' +
                    green + u'\u001b[12C' + '  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + yellow +
                    '▓▓▓▓▓▓▓▓▓▓▓  \n' + green + u'\u001b[12C' +
                    '    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + yellow + '▓▓▓▓▓▓▓▓▓▓▓    \n' +
                    green + u'\u001b[12C' + '     ▓▓▓▓▓▓▓▓▓▓▓▓▓' + yellow +
                    '▓▓▓▓▓▓▓▓▓▓▓     \n' + green + u'\u001b[12C' +
                    '        ▓▓▓▓▓▓▓▓▓' + yellow + '▓▓▓▓▓▓▓▓▓        \n' +
                    green + u'\u001b[12C' + '            ▓▓▓▓' + yellow +
                    '▓▓▓▓▓▓            \n' + colour2)
                input(u'\u001b[20C' + "(Enter to Continue)")
    ###end of while loop###


def game_colour(console, current):
    """
    This function changes the text and screen colours for the game.
    
    ## Args
    console: str
    
    current: str

    ## Returns
    new: str
    
    console or current: str
    
    new1, new2: str
    """
    option = ''
    new1 = console
    new2 = current
    new = ''
    #start of new screen
    screen(console, current)
    stdout.write(current + u'\u001b[20A' + u'\u001b[18C' +
                 'Colour Settings:\n' + u'\u001b[18C' +
                 '(s) - Change screen \n' + u'\u001b[18C' +
                 '(t) - Change text\n')
    option = input(u'\u001b[18C')

    if option == 't':
        ##start of for loop##
        for i in range(len(colourOptions)):
            #displays the purchased colours
            stdout.write(u'\u001b[18C' +
                         '({}) - {}\n'.format(i, colourOptions[i]) + colour2)
        ##end of for loop##
        option = input(u'\u001b[18C')
        #checks if the input was valid. If it is not, then nothing happens. If it is, then the text colour will change.
        if option.isdigit() == False:
            return new1, new2
        elif option.isdigit() and int(option) >= len(colourOptions):
            return new1, new2
        elif option.isdigit() == True and int(option) <= len(colourOptions):
            if colourOptions[int(option)] == 'none':
                new = '\u001b[0m'
            elif colourOptions[int(option)] == 'green':
                new = '\u001b[38;2;0;225;0m'
            elif colourOptions[int(option)] == 'red':
                new = '\u001b[38;2;250;80;50m'
            elif colourOptions[int(option)] == 'yellow':
                new = u'\u001b[38;2;255;255;0m'
            elif colourOptions[int(option)] == 'grey':
                new = '\u001b[38;2;175;175;175m'
            elif colourOptions[int(option)] == 'blue':
                new = u'\u001b[38;2;45;90;250m'
            elif colourOptions[int(option)] == 'turquoise':
                new = u'\u001b[38;2;15;235;145m'
            return console, new
    elif option == 's':
        ##start of for loop##
        for i in range(len(colourOptions)):
            #displays the purchased colours
            stdout.write(u'\u001b[18C' +
                         '({}) - {}\n'.format(i, colourOptions[i]) + colour2)
        ##end of for loop##
        option = input(u'\u001b[18C')
        #checks if the input was valid. If it is not, then nothing happens. If it is, then the text colour will change.
        if option.isdigit() == False:
            return new1, new2
        elif option.isdigit() and int(option) >= len(colourOptions):
            return new1, new2
        elif option.isdigit() == True and int(option) <= len(colourOptions):
            if colourOptions[int(option)] == 'none':
                new = '\u001b[0m'
            elif colourOptions[int(option)] == 'green':
                new = '\u001b[38;2;0;225;0m'
            elif colourOptions[int(option)] == 'red':
                new = '\u001b[38;2;250;80;50m'
            elif colourOptions[int(option)] == 'yellow':
                new = u'\u001b[38;2;255;255;0m'
            elif colourOptions[int(option)] == 'grey':
                new = '\u001b[38;2;175;175;175m'
            elif colourOptions[int(option)] == 'blue':
                new = u'\u001b[38;2;45;90;250m'
            elif colourOptions[int(option)] == 'turquoise':
                new = u'\u001b[38;2;15;235;145m'
            return new, current
    else:
        return new1, new2


#### START OF MAIN CODE ####
#adds the colour green as a variable
green = '\u001b[38;2;0;225;0m'
#adds the colour red as a variable
red = '\u001b[38;2;250;80;50m'
#adds the colour grey as a variable
grey = '\u001b[38;2;175;175;175m'
#adds the colour yellow as a variable
yellow = u'\u001b[38;2;255;255;0m'
#adds the colour brown as a variable
brown = u'\u001b[38;2;135;100;15m'
#adds the colour blue as a variable
blue = u'\u001b[38;2;45;90;250m'
#adds the colour turquoise as a variable
turquoise = u'\u001b[38;2;15;235;145m'
#adds the colour white as a variable
white = u'\u001b[38;2;255;255;255m'
#resets the colour as a variable
reset = '\u001b[0m'
#sets play as nothing for the start of the game
play = ''
#sets game as 0 for the start of the game
game = 0
#sets what games are unlocked at the start of the game
games = [1,2,3]  #default games are 1,2,3
#sets the score to be 0 at the start of the game
score = 0
#sets what art is unlocked
art = []
#sets the different art that can be purchased
artOptions = ['Tree', 'Cactus', 'Game System', 'Chrome Logo']
#sets starting colour2 to be green
colour2 = green
colour1 = reset
#list of available colours for the text in the game
colourOptions = ['none', 'green']
#starts the welcome screen to the game
welcome(colour1, colour2)
###start of while loop###
while True:
    ##start of while loop##
    while play != 'q':
        play = ''
        game = ''
        if score == None:
            score = 0
        #start of new screen
        screen(colour1, colour2)
        #displays the score and the different menu options
        stdout.write(u'\u001b[20A' + u'\u001b[18C' + colour2 + 'score:' +
                     str(score) + "\n\n" + u'\u001b[18C' +
                     '(g) - play game\n' + u'\u001b[18C' +
                     '(s) - go to shop\n')
        #checks if any art has been purchased
        if len(art) > 0:
            stdout.write(u'\u001b[18C' + '(a) - view artwork\n')
        stdout.write(u'\u001b[18C' + '(p) - play specific games\n' +
                     u'\u001b[18C' + '(o) - change text colour\n' +
                     u'\u001b[18C' + '(q) - Exit\n' + u'\u001b[18C')
        stdout.flush()
        play = input().lower()
        if play == 'o':
            colour1, colour2 = game_colour(colour1, colour2)
            screen(colour1, colour2)
        #checks what menu item the user selected
        elif play == 'g':
            #chooses a random game from the games unlocked
            game = choice(games)
            if game == 1:
                score = numbers(score, colour1, colour2)
            elif game == 2:
                score = patterns(score, colour1, colour2)
            elif game == 3:
                score = memory(score, colour1, colour2)
            elif game == 4:
                score = RockPaperScissors(score, colour1, colour2)
            elif game == 5:
                score = coin_flip(score, colour1, colour2)
            elif game == 6:
                score = even_or_odd(score, colour1, colour2)
            elif game == 7:
                score = blackjack(score, colour1, colour2)
            elif game == 8:
                score = dice(score, colour1, colour2)
            elif game == 9:
                score = roulette(score, colour1, colour2)
            elif game == 10:
                score = spin(score, colour1, colour2)
            game = 0
            play = ''
        elif play == 's':
            score = store(score, colour1, colour2)
            play = ''
        elif play == 'a' and len(art) > 0:
            artwork(colour1, colour2)
            play = ''
        elif play == 'p':
            #start of while loop#
            while game != 'e':
                #start of new screen
                screen(colour1, colour2)
                #prints the score and the games that have been unlocked
                stdout.write(u'\u001b[20A' + u'\u001b[18C' + colour2 +
                             'score:' + str(score) + "\n\n")
                if 1 in games:
                    stdout.write(u'\u001b[18C' + '(1) - math\n')
                if 2 in games:
                    stdout.write(u'\u001b[18C' + '(2) - patterns\n')
                if 3 in games:
                    stdout.write(u'\u001b[18C' + '(3) - memory\n')
                if 4 in games:
                    stdout.write(u'\u001b[18C' + '(4) - rock, paper, scissors\n')
                if 5 in games:
                    stdout.write(u'\u001b[18C' + '(5) - coin flip\n')
                if 6 in games:
                    stdout.write(u'\u001b[18C' + '(6) - even or odd\n')
                if 7 in games:
                    stdout.write(u'\u001b[18C' + '(7) - blackjack\n')
                if 8 in games:
                    stdout.write(u'\u001b[18C' + '(8) - dice\n')
                if 9 in games:
                    stdout.write(u'\u001b[18C' + '(9) - roulette\n')
                if 10 in games:
                    stdout.write(u'\u001b[18C' + '(10) - slot machine\n')
                stdout.write(u'\u001b[18C' + '(e) - Exit menu\n')

                game = input(u'\u001b[18C' + 'Select a game to play:' + '\n' +
                             u'\u001b[18C')
                #selects the game that the user chose if the game is unlocked
                if game == '1':
                    score = numbers(score, colour1, colour2)
                elif game == '2':
                    score = patterns(score, colour1, colour2)
                elif game == '3':
                    score = memory(score, colour1, colour2)
                elif game == '4' and 4 in games:
                    score = RockPaperScissors(score, colour1, colour2)
                elif game == '5' and 5 in games:
                    score = coin_flip(score, colour1, colour2)
                elif game == '6' and 6 in games:
                    score = even_or_odd(score, colour1, colour2)
                elif game == '7' and 7 in games:
                    score = blackjack(score, colour1, colour2)
                elif game == '8' and 8 in games:
                    score = dice(score, colour1, colour2)
                elif game == '9' and 9 in games:
                    score = roulette(score, colour1, colour2)
                elif game == '10' and 10 in games:
                    score = spin(score, colour1, colour2)
            #end of while loop#
    else:
        #start of new screen
        screen(colour1, colour2)
        #asks the user if they really want to quit
        #if the user doesn't input yes, then returns to the main menu
        if input(u'\u001b[20A' + u'\u001b[23C' + "Exit?\n" + u'\u001b[23C' +
                 "Y / N\n" +
                 u'\u001b[25C').lower() in ['y', 'Y', 'yes', 'Yes', 'YES']:
            #if the user does quit, their final score is displayed
            stdout.write(u'\u001b[18C' + 'Final Score: {}\n'.format(score))
            if score > 0:
                stdout.write(u'\u001b[20C' + 'Good Bye!\n' + u'\u001b[23C')
            else:
                stdout.write(u'\u001b[20C' + 'Try again!\n' + u'\u001b[23C')
            break
    ##end of while loop##
        else:
            play = ''
###end of while loop###
#### END OF MAIN CODE ####