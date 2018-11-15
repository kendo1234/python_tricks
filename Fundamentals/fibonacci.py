from functools import lru_cache  # lru stands for - least recently used


# 1, 1, 2, 3, 5, 8, 13, 21 and so on..
# Write a function to return the nth term of Fibonnaci


# recursive function, calling itself
# Memoization - caching of values to eliminated repeated resource useage
@lru_cache(maxsize=1000)
def fibonnacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonnacci(n - 1) + fibonnacci(n - 2)


for n in range(1, 501):
    print(n, ":", fibonnacci(n))
