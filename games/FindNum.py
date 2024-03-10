from os import system
from msvcrt import getch
from time import sleep

def num_finder():
    l1 = [x for x in range(1,64,2)]
    l2 = [x for x in range(2,63,4)] + [x for x in range(3,64,4)] ; l2.sort()
    l3 = [x for x in range(4,63,8)] + [x for x in range(5,64,8)] + [x for x in range(6,64,8)] + [x for x in range(7,64,8)] ; l3.sort()
    l4 = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,63]
    l5 = [x for x in range(16,32)] + [x for x in range(48,64)]
    l6 = [x for x in range(31,62)]

    li = [l1, l2, l3, l4, l5, l6]

    system("cls")
    print(60*"=-")
    print("choose a number between 1 , 63 and keep it in your mind".center(120))
    print("I'll ask you some questions and find your number ...".center(120))

    print("press any key to continue ...".center(120, "*"))
    getch()

    number = 0
    for i in range(6):
        system("cls")
        print(str(li[i]).center(120))
        print()
        print("do you see your chosen number here?".center(120))
        ans = input(60*" ")
        if ans == "y":
            number += (2**i)
            system("cls")
        system("cls")
        print(120*".")
    return number



def main():
    founded_num = num_finder()
    for i in range(5,0,-1):
        system("cls")
        print (f"{i} seconds to find your number ...".center(120))
        sleep(1)
    system("cls")
    print(f"your number is {founded_num}".center(120))


if __name__ == "__main__":
    main()
