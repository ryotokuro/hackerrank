# two cats and a mouse at position on a line
# determine which cat reaches the mouse first
# cats travel at equal speed
#   - if arrive at same time
#       mouse can move and escapes while they fight

# given q queries in form x, y, z
#   x - position cat A
#   y - position cat B
#   z - position mouse

# output:
# if cat a wins: print "Cat A"
# if cat b wins: print "Cat B"
# if both same: print "Mouse C"


def catAndMouse(catAPos, catBPos, numOfQueries):
    # for i in range(numOfQueries):
    state = "Mouse C"
    if catAPos > catBPos:
        state = "Cat A"

    elif catBPos > catBPos:
        state = "Cat B"

    return state


# input
# FIRST LINE: integer denoting number of queries
numOfQueries = int(input())
# SECOND LINE: 3 space separated ints - describing x, y, z (see above)
# catAPos = catBPos = []
for i in range(numOfQueries):
    catAPos, catBPos, mousePos = map(int, input().strip().split(' '))
    print(catAndMouse(catAPos, catBPos, numOfQueries))
# catAPos.append()
# catBPos

