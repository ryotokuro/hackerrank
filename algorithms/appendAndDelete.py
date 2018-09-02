# PROBLEM
# You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:
#   1. Append a lowercase English alphabetic letter to the end of the string.
#   2. Delete the last character in the string. Performing this operation on an empty string results in an empty string.
#
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t
# by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.

# EXAMPLE
# strings s = [a, b, c] and t = [d, e, f].
# Our number of moves, k = 6.
#
# To convert s to t, we first delete all of the characters in 3 moves.
# Next we add each of the characters of t in order. On the 6th move, you will have the matching string. If there
# had been more moves available, they could have been eliminated by performing multiple deletions on an empty string.
# If there were fewer than 6 moves, we would not have succeeded in creating the new string.
