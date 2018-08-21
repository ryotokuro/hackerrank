# BACKGROUND
# Aerith is playing a cloud hopping game. In this game, there are sequentially
# numbered clouds that can be thunderheads or cumulus clouds.
# Her character must jump from cloud to cloud until it reaches the start again.

# PROBLEM
# To play, Aerith is given an array of clouds, c and an energy level e = 100.
# She starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k) % n].
# If Aerith lands on a thundercloud, c[i] = 1, her energy (e) decreases by 2 additional units.
# The game ends when Aerith lands back on cloud 0.

# Given the values of n, k, and the configuration of the clouds as an array c,
# - Can you determine the final value of e after the game ends?

# EXAMPLE
# For example, give c = [0, 0, 1, 0] and k = 2, the indices of her path are 0 -> 2 -> 0.
# Her energy level reduces by 1 for each jump to 98. She landed on one thunderhead
# at an additional cost of 2 energy units. Her final energy level is 96.

# NOTE: Note: Recall that % refers to the modulo operation. In this case, it serves
# to make the route circular. If Aerith is at c[n-1] and jumps 1, she will arrive at 0.

# FUNCTION DESCRIPTION
# It should return an integer representing the energy level remaining after the game.
# jumpingOnClouds has the following parameter(s):
#   - c: an array of integers representing cloud types
#   - k: an integer representing the length of one jump
