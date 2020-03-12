# https://www.hackerrank.com/challenges/py-if-else/problem
# Task
# Given an integer, n, perform the following conditional actions:
# If "n" is odd, print Weird
# If "n" is even and in the inclusive range of 2 to 5, print Not Weird
# If "n" is even and in the inclusive range of 6 to 20, print Weird
# If "n" is even and greater than 20, print Not Weird
# Input Format : A single line containing a positive integer, "n" .
# Constraints : 1<= "n" <= 100
# Output Format : Print Weird if the number is weird; otherwise, print Not Weird.

n = int(input())
if n < 1 and n > 100:
    exit(1)
elif n % 2 == 0 and n > 20:
    print("Not Weird")
elif n % 2 == 0 and n > 6:
    print("Weird")
elif n % 2 == 0 and n > 2 and n < 5:
    print("Not Weird")
else:
    print("Weird")
