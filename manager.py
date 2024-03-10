from games.tic_tac_toe import main as t_main
from games.rps import main as r_main
from games.FindNum import main as find_main
from os import system
from msvcrt import getch

while True:
    system("cls")
    print(60*"=-")
    print("[1]tic tac toe [2]rock paper sciccor".center(120))
    print("[3]find the number".center(120))
    choice = input("enter your choice: ".center(120))

    if choice == "1":
        system("cls")
        t_main()
        getch()
    elif choice == "2":
        system("cls")
        r_main()
        getch()
    elif choice == "3":
        system("cls")
        find_main()
        getch()
    else:
        system("cls")
        print("please enter a valid choice!!".center(120))
        print("press ENTER".center(120))
        getch()


        

