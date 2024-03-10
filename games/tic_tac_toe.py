from random import randint, choice
from time import sleep
from os import system

# -------------------------------------------------------------------

game_page = [
#    1    2    3
    '_', '_', '_', # a
    '_', '_', '_', # b
    '_', '_', '_' # c
]

# -------------------------------------------------------------------

def printer():
    print("    1        2        3".center(120))
    print(f"a  [  {game_page[0]}  ]  [  {game_page[1]}  ]  [  {game_page[2]}  ]".center(120), sep="  ", end="\n\n")
    print(f"b  [  {game_page[3]}  ]  [  {game_page[4]}  ]  [  {game_page[5]}  ]".center(120), sep="  ", end="\n\n")
    print(f"c  [  {game_page[6]}  ]  [  {game_page[7]}  ]  [  {game_page[8]}  ]".center(120), sep="  ", end="\n\n")
    print("-" * 120)

# -------------------------------------------------------------------

def game():
    print()
    while True:
        system("cls")
        printer()
        print()
        print("---your turn---".center(120))
        print()
        print("enter your move: ".center(120))
        user_move = input(60*" ")
        if user_move == "a1":
            user_move = 1
        elif user_move == "a2":
            user_move = 2
        elif user_move == "a3":
            user_move = 3
        elif user_move == "b1":
            user_move = 4
        elif user_move == "b2":
            user_move = 5
        elif user_move == "b3":
            user_move = 6
        elif user_move == "c1":
            user_move = 7
        elif user_move == "c2":
            user_move = 8
        elif user_move == "c3":
            user_move = 9

        if game_page[int(user_move)-1] == "_":
            game_page[int(user_move)-1] = "O"
            break
    result , winner = checker()
    if result:
        return winner
    system("cls")
    printer()
    sleep(1)
    system("cls")

    print("-"*120)
    print("-computer turn -".center(120))
    # print("-"*120)

    sleep(1.5)

    while True:
        computer_choice = choice(game_page)
        if computer_choice == "_":
            game_page[game_page.index(computer_choice)] = "X"
            break
    printer()
    sleep(1)

    result , winner = checker()
    if result:
        return winner
    
    # printer()

    return None


# -------------------------------------------------------------------

def checker():
    for i in range(0, 9, 3):
        if game_page[i] != "_":
            if game_page[i] == game_page[i+1] == game_page[i+2]:
                return True , game_page[i]
            
    for i in range(3):
        if game_page[i] != "_":
            if game_page[i] == game_page[i+3] == game_page[i+6]:
                return True , game_page[i]
            
    if game_page[0] != "_":
        if game_page[0] == game_page[4] == game_page[8]:
            return True , game_page[0]
        
    if game_page[2] != "_":
        if game_page[2] == game_page[4] == game_page[6]:
            return True , game_page[0]
        
    return None , "_"
    
# -------------------------------------------------------------------

def main():
    res = "no one"
    printer()
    while True:
        res = game()
        if res != None:
            break
    system("cls")
    printer()
    print("= "*60)
    if res == "O":
        print("you win!!!!!".center(120))
    else:
        print("you lose!!!!".center(120))
    again = input("do you want to play again?(y/n)".center(120))
    if again.lower() == "y":
        main()
    else:
        system("cls")
        print("good luck!".center(120))
        sleep(2)


if __name__ == "__main__":
    main()

