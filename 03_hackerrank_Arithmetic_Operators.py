# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
a = int(input())
b = int(input())
if (a >= 10**10 or b >= 10**10):
    exit(1)
else:
    print(a+b)
    print(a-b)
    print(a*b)
