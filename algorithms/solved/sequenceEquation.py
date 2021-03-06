# import os
# SOLVED: https://www.hackerrank.com/challenges/permutation-equation/problem

# You are given a sequence of  integers:
# p(1), p(2), ..., p(n)
# Each element in the sequence is distinct and satisfies 1 <= p(x) <= n

# PROBLEM
# For each x where 1 <= x <= n, find any integer y such that p(p(y)) === x and print value y on a new line

# EXAMPLE
# Given sequence p = [5 2 1 3 4] For each value of x between 1 and 5, we analyse:
# * x=1 : p[3],p[4] = 3 so p[p[4]] = 1
# * x=2 : p[2],p[2] = 2 so p[p[2]] = 2
# * x=3 : p[4],p[5] = 4 so p[p[5]] = 3
# * x=4 : p[5],p[1] = 5 so p[p[1]] = 4
# * x=5 : p[1],p[3] = 3 so p[p[3]] = 5
# Essentially, the format is y = [p[location of number wanted in sequence], p[location of location address]]
#
# Therefore, we find the values [4 2 5 1 3] for y

global x
x = 1


def permutationEquation(pList):
    global x

    i = pList.index(x)
    yAddress = pList.index(i+1)

    for i in range(len(pList)):
        # find where is x = 1?
        if pList[i] == x:
            yAddress = i+1
            break

    # now find where that yaddress is
    for j in range(len(pList)):
        if pList[j] == yAddress:
            yAddress = j+1
            break

    x += 1
    return yAddress


# INPUT
# The first line contains an integer N, the number of elements in the sequence.
numElements = int(input())

# The second line contains N space-separated integers p[i] where 1 <= i <= n.
p = list(map(int, input().strip().split(' ')))

# OUTPUT
# For each x from 1 to n, print an integer denoting any valid y satisfying the equation p(p(y)) === x on a new line.
for i in range(numElements):
    print(permutationEquation(p))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     numElements = int(input())
#
#     p = list(map(int, input().rstrip().split()))
#
#     for i in range(numElements):
#         result = permutationEquation(p)
#
#         fptr.write(str(result))
#         fptr.write('\n')
#
#     fptr.close()