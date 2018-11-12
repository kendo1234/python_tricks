# itertools.permutations() generates permutations
# for an iterable. Time to brute-force those passwords ;-)
import itertools


def password_permutations(passWord):
    for p in itertools.permutations(passWord):
        print(p)


print('Please Enter Password to Calculate Permutations:')
passW = input()
password_permutations(passW)
