# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
a = int(input())
b = int(input())
if (a >= 10000000000 or b >= 10000000000):
    exit(1)
else:
    print(a+b)
    print(a-b)
    print(a*b)
