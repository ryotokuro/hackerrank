# HACKER RANK CHALLENGE: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# CLOSED: working solution :)

# Lily likes to play games with integers.
# She has created a new game where she determines the difference between a number and its reverse.

# For instance, given the number 12,
# -> its reverse is 21.
# -> Their difference is 9.
#
# The number 120 reversed is 12, and their difference is 99.

# She decides to apply her game to decision making.
# She will look at a numbered range of days and will only go to a movie on a beautiful day.

# Determine the number of days in the range that are beautiful given:
# - range of numbered days, [i...j]
# - and a number k
# * Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k.
# If a day's value is a beautiful number, it is a beautiful day.
# Print the number of beautiful days in the range.


def beautifulDays(startDay, endDay, divCriteria):
    goodDays = 0
    for day in range(startDay, endDay+1):
        # reverseDay = int("".join(list(reversed(str(day)))))
        if abs(day - int("".join(list(reversed(str(day)))))) % divCriteria == 0:
            goodDays += 1

    return goodDays


# INPUT
# A single line of three space-separated integers describing the respective values of i, j, k
startDay, endDay, divCriteria = map(int, input().strip().split(' '))

# OUTPUT
# Print the number of beautiful days in the inclusive range between i and j.
print(beautifulDays(startDay, endDay, divCriteria))