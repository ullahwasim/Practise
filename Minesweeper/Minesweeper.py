import numpy as np
from random import randint
import sys

def check(C, B, temp_1, temp_2):
    if C[temp_1][temp_2] != 9:
        for i in range(max(0, temp_1 - 1), min(r - 1, temp_1 + 1) + 1):
            for j in range(max(0, temp_2 - 1), min(c - 1, temp_2 + 1) + 1):
                if C[i][j] == 0 and B[i][j] == '-':
                    B[i][j] = str(0)
                    check(C, B, i, j)
                elif C[i][j] != 9:
                    B[i][j] = str(C[i][j])


def Welcome():
    print("Welcome To Minesweeper")


def LoopCreateMatrix(r,c):
    place_mines = 0
    while True:
        mines = int(input("Enter Number Of Mines\n"))
        if r*c > mines:
            break;
        else:
            print("Mines value should be lower")
    print("Mines will be represented as '9'\n")
    C = np.zeros((r, c))
    while place_mines < mines:
        temp_1 = randint(0, r - 1)
        temp_2 = randint(0, c - 1)
        for i in range(max(0, temp_1 - 1), min(r - 1, temp_1 + 1) + 1):
            for j in range(max(0, temp_2 - 1), min(c - 1, temp_2 + 1) + 1):
                if C[i][j] != 9:
                    if i == temp_1 and j == temp_2:
                        place_mines += 1
                        C[i][j] = 9
                    else:
                        C[i][j] += 1
    return C


if __name__ == '__main__':
    Welcome()
    r = int(input('Enter Rows Of Minesweeper\n'))
    c = int(input('Enter Columns Of Minesweeper\n'))
    C = LoopCreateMatrix(r,c)
    B = np.full((r, c), '-')
    sys.stdout.write(' ')
    for i in range(0,c):
        sys.stdout.write(' '+str(i))
    print()
    for i, row in enumerate(B):
        print(i, ' '.join(row))
    while True:
        i = 0
        j = 0
        flag = False
        temp_1 = int(input('Enter Row\n'))
        temp_2 = int(input('Enter Column\n'))
        if C[temp_1][temp_2] == 9:
            print(C)
            print("Game Over")
            break
        else:
            check(C, B, temp_1, temp_2)
            for i in range(0, r):
                for j in range(0, c):
                    if B[i][j] == '-' and C[i][j] != 9:
                        flag = True
                        break
                if flag:
                    break
            if i == r - 1 and j == c - 1:
                print(C)
                print("You Won!")
                break
            sys.stdout.write(' ')
            for i in range(0, c):
                sys.stdout.write(' ' + str(i))
            print()
            for i, row in enumerate(B):
                print(i, ' '.join(row))
