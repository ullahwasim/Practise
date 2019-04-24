from random import randint
import numpy as np
import sys
from heapq import nsmallest
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


def findindexes(a):
    seen, indexes = set(), []
    for idx, item in enumerate(a):
        if item not in seen:
            seen.add(item)  # First time seeing the element
        else:
            indexes.append(idx)  # Already seen, add the index to the result
    return indexes


def fitnessfucntion(chromosome, n):
    attactingpairs = [0, 0, 0, 0]
    for i in range(0, 4):
        k = 0
        z = 0
        while k < n:
            j = 0
            z = k
            while j < n - 1:
                if chromosome[i][j] == chromosome[i][z] and j != z:
                    attactingpairs[i] += 1
                j += 1
            j = k
            temp_j = j
            x = 0
            while temp_j < n:
                x += 1
                temp_j += 1
                if temp_j < n:
                    if chromosome[i][j] == chromosome[i][temp_j] - x or chromosome[i][j] == chromosome[i][temp_j] + x:
                        attactingpairs[i] += 1
            temp_j = j
            x = 0
            while temp_j > -1:
                x += 1
                temp_j -= 1
                if temp_j > -1:
                    if (chromosome[i][j] == chromosome[i][temp_j] - x or chromosome[i][j] == chromosome[i][temp_j] + x):
                        attactingpairs[i] += 1
            k += 1

    return attactingpairs


def is_a_in_x(A, X):
    if A == None:
        return False
    for i in range(len(X) - len(A) + 1):
        if A == X[i:i + len(A)]: return True
    return False


if __name__ == '__main__':
    n = Welcome()
    count = 0
    count1 = 0
    temp7 = None
    # chromosome = [[0] * n]*4
    chromosome = []
    for i in range(0, 4):
        chromosome.append([])
        for j in range(0, n):
            ran = randint(0, n - 1)
            chromosome[i].append(ran)
    while True:
        print("Population is ")
        print(chromosome)
        B = np.full((n, n), '-')
        print("First Chromosome is ")
        for i in range(0, n):
            B[chromosome[0][i]][i] = 1
        sys.stdout.write(' ')
        for k in range(0, n):
            sys.stdout.write(' ' + str(k))
        print()
        for k, row in enumerate(B):
            print(k, ' '.join(row))

        print("Second Chromosome is ")
        B1 = np.full((n, n), '-')
        for i in range(0, n):
            B1[chromosome[1][i]][i] = 1
        sys.stdout.write(' ')
        for k in range(0, n):
            sys.stdout.write(' ' + str(k))
        print()
        for k, row in enumerate(B1):
            print(k, ' '.join(row))

        print("Third Chromosome is ")
        B2 = np.full((n, n), '-')
        for i in range(0, n):
            B2[chromosome[2][i]][i] = 1
        sys.stdout.write(' ')
        for k in range(0, n):
            sys.stdout.write(' ' + str(k))
        print()
        for k, row in enumerate(B2):
            print(k, ' '.join(row))

        print("Fourth Chromosome is ")
        B3 = np.full((n, n), '-')
        for i in range(0, n):
            B3[chromosome[3][i]][i] = 1
        sys.stdout.write(' ')
        for k in range(0, n):
            sys.stdout.write(' ' + str(k))
        print()
        for k, row in enumerate(B3):
            print(k, ' '.join(row))
        attactingpairs = fitnessfucntion(chromosome, n)

        print("Fitness values is ")
        print(attactingpairs)
        temp1 = copy.deepcopy(attactingpairs)
        smallest_3 = nsmallest(3, temp1)
        print("Testing")
        print(smallest_3)
        index1 = []
        index1.append(temp1.index(smallest_3[0]))
        temp1[index1[0]] = 100000
        print(temp1)
        index1.append(temp1.index(smallest_3[1]))
        temp1[index1[1]] = 100000
        index1.append(temp1.index(smallest_3[2]))
        print("Three lowest fittest values in terms of index")
        print(index1)
        if smallest_3[0] == 0:
            print("Solution is ")
            print(chromosome[index1[0]])

            B5 = np.full((n, n), '-')
            for i in range(0, n):
                B5[chromosome[index1[0]][i]][i] = 1
            sys.stdout.write(' ')
            for k in range(0, n):
                sys.stdout.write(' ' + str(k))
            print()
            for k, row in enumerate(B5):
                print(k, ' '.join(row))
            break

        count1 += 1
        if count1 == 10000:
            print("Fittness values is ")
            print(attactingpairs)
            print("Cannot improve fitness values more as reach at local maxima Please rerun the program for solution")
            break
        if count == 20:
            print("Fittness values is ")
            print(attactingpairs)
            print("Cannot improve fitness values more as reach at local maxima Please rerun the program for solution")
            break
        if is_a_in_x(temp7, attactingpairs):
            count += 1
        # else:
        #    count=0
        temp7 = copy.deepcopy(attactingpairs)
        print("Doing Crossover")
        chromosome1 = []
        chromosome1.append([])
        chromosome1.append([])
        chromosome1.append([])
        chromosome1.append([])

        first, middle, last = [chromosome[index1[0]], chromosome[index1[1]], chromosome[index1[2]]]

        b = [
            first[:-int(n / 2)] + middle[-int(n / 2):],
            middle[:-int(n / 2)] + first[-int(n / 2):],

            middle[:-int(n / 2)] + last[-int(n / 2):],
            last[:-int(n / 2)] + middle[-int(n / 2):],
        ]
        print(b)
        for j in range(0, 4):
            indexes = findindexes(b[j])
            if len(indexes) != 0:
                for i in range(0, n):
                    if i not in b[j]:
                        b[j][indexes[0]] = i

            else:
                ran = randint(0, n - 1)
                ran1 = randint(0, n - 1)
                b[j][ran], b[j][ran1] = b[j][ran1], b[j][ran]
        print("Doing Mutation")
        print("Updated Population")
        # print(chromosome1)
        print(b)
        chromosome = None
        # chromosome=copy.deepcopy(chromosome1)
        chromosome = copy.deepcopy(b)
