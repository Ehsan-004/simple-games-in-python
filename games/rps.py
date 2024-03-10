from random import choice
from os import system

def rps(times):
    l = ["rock", "paper", "sciccors"]
    user_score = 0 
    com_score = 0 

    for i in range(times):
        moves = []
        print(120*"-")
        print("[1]rock [2]paper [3]sciccors [4]exit".center(120))
        print(120*"-")

        user_move = input("your choice: ".center(120))
        system("cls")
        if user_move == "1":
            print(f"your choice : rock".center(120))
            moves.append("rock")
        elif user_move == "2":
            print(f"your choice : paper".center(120))
            moves.append("paper")
        elif user_move == "3":
            print(f"your choice : sciccors".center(120))
            moves.append("sciccors")
        elif user_move == "c" or user_move == "4" :
            return "break"
        else:
            moves.append(user_move.lower())

        com_input = choice(l)
        moves.append(com_input)
        print(f"computer choice : {com_input}".center(120))
        
        
        if "rock" in moves and "sciccors" in moves:
            if moves.index("rock") == 0:
                print()
                print("you got 1 score!".center(120,"-"))
                print()
                user_score += 1
            else:
                print("computer got 1 score!".center(120, "-"))
                com_score += 1

        elif "rock" in moves and "paper" in moves:
            if moves.index("paper") == 0:
                print()
                print("you got 1 score!".center(120,"-"))
                print()
                user_score += 1
            else:
                print()
                print("computer got 1 score!".center(120, "-"))
                print()
                com_score += 1
        elif "paper" in moves and "sciccors" in moves:
            if moves.index("sciccors") == 0:
                print()
                print("you got 1 score!".center(120,"-"))
                print()
                user_score += 1
            else:
                print()
                print( "computer got 1 score!".center(120, "-"))
                print()
                com_score += 1
        print("your score | computer score".center(120))
        print(f"{user_score}          {com_score}".center(120))
        # print("%-10i"%user_score)
        
    if user_score > com_score :
        return "user"                
    elif user_score < com_score :
        return "computer"
    else:
        return "equal"
    

def main():
    while True:
        system("cls")
        print("how many times would you like to play?".center(120))
        times = int(input("".center(60)))    
        system("cls")
        if (winner := rps(times)) != "equal":
            print("winner is ", winner)
        elif winner == "break":
            print("you stopped the game!")
        else:
            print("No one won!")

        if (ans := input("woukd you like to play again (y/n) ?").lower()) == "n":
            break
        elif ans == "y":
            pass
    

if __name__ == "__main__":
    main()




