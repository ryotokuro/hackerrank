from collections import defaultdict

# number of test cases
t = int(input())
tests = {}

for _ in range(t):
    # get space separated input
    # 1. n - defines set length S where S = {1, 2, 3, ... n}
    # 2. k - maximum size of number
    n, k = map(int, input().split())
    tests[n] = k

# sorted(tests) gives the keys in numerical order
largest = sorted(tests)[-1]  # the last one is the largest
print(largest)  

store = defaultdict(list)
for i in range(1, largest):
    for j in range(i+1, largest+1):
        if i&j not in store[j]:
            store[j].append(i&j)
print(store)

for i in tests.keys():
    print([store[j] for j in range(2, i+1)])
"""
answer = None
for i in range(1, n):
    for j in range(i+1, n+1):
        # print(i, 'AND', j, '=', i&j)
        if i&j > answer and i&j < k:
            answer = i&j
print(answer)
"""

# instead of doing it in real-time
# store the test numbers first

# then compute results for largest number (e.g. 999 is one test so nest for loop up to 999)
# then go through stored test numbers (loop) and slice the dictionary
# do a lookup for largest number smaller than k
# print answer
