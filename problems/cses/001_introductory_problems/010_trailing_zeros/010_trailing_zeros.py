# https://cses.fi/problemset/task/1618

n = int(input())

trailing_zeros = 0
divider = 5

while divider <= n:
    trailing_zeros += n // divider
    divider *= 5

print(trailing_zeros)
