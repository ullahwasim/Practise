import numpy as np
import random
import sys
import copy


def Welcome():
    print("Welcome To N Queen Problem")
    while True:
        n = int(input('Enter N Of N Queen Problem\n'))
        if n < 4:
            print("N Should be greater than 3")
        else:
            break
    return n


def editdomain(dict, temp, c, n):
    c += 1
    r1 = temp - 1
    r2 = temp + 1
    if -1 < c < n and -1 < r1 < n:
        if dict['Q' + str(c)].__contains__(r1):
            dict['Q' + str(c)].remove(r1)
    if -1 < c < n and -1 < r2 < n:
        if dict['Q' + str(c)].__contains__(r2):
            dict['Q' + str(c)].remove(r2)


def editdomain1(dict, temp, c, n):
    c += 1
    r1 = temp - 1
    if -1 < c < n and -1 < r1 < n:
        if dict['Q' + str(c)].__contains__(r1):
            dict['Q' + str(c)].remove(r1)


def editdomain2(dict, temp, c, n):
    c += 1
    r2 = temp + 1
    if -1 < c < n and -1 < r2 < n:
        if dict['Q' + str(c)].__contains__(r2):
            dict['Q' + str(c)].remove(r2)


if __name__ == '__main__':
    n = Welcome()
    B = np.full((n, n), '-')
    sys.stdout.write(' ')
    for i in range(0, n):
        sys.stdout.write(' ' + str(i))
    print()
    for i, row in enumerate(B):
        print(i, ' '.join(row))
    dict = {}
    for i in range(0, n):
        dict['Q' + str(i)] = [j for j in range(0, n)]
    print("Domain Of Queens")
    print(dict)
    list = []
    list.append(dict.copy())
    i = 0
    temp3 = []
    flag = False
    while -1 < i < n:
        if flag:
            m = temp3.pop()
            B[m][i] = '-'
            flag = False
        dict = None
        print(list[i])
        # dict=list[i].copy()
        dict = copy.deepcopy(list[i])
        if dict['Q' + str(i)].__len__() == 0:
            flag = True
            i -= 1
            list.pop()
            continue
        temp_1 = random.choice(dict['Q' + str(i)])
        dict['Q' + str(i)].remove(temp_1)
        list.pop()
        # list.append(dict.copy())
        list.append(copy.deepcopy(dict))
        for j in range(i, n):
            if dict['Q' + str(j)].__contains__(temp_1):
                dict['Q' + str(j)].remove(temp_1)
        B[temp_1][i] = 1
        temp3.append(temp_1)
        temp1 = temp_1
        temp2 = temp_1
        c = i
        editdomain(dict, temp_1, c, n)
        while True:
            c += 1
            temp1 -= 1
            if (temp1 < -1 and c >= n):
                break
            else:
                editdomain1(dict, temp1, c, n)
        c = i
        while True:
            c += 1
            temp2 += 1
            if (temp2 >= n and c >= n):
                break
            else:
                editdomain2(dict, temp2, c, n)
        sys.stdout.write(' ')
        for k in range(0, n):
            sys.stdout.write(' ' + str(k))
        print()
        for k, row in enumerate(B):
            print(k, ' '.join(row))
        print("Domain Of Queens")
        print(dict)
        i += 1
        # list.append(dict.copy())
        list.append(copy.deepcopy(dict))