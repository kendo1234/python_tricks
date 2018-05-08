xs = {'a':1, 'b':2, 'c':3, 'd':4}


# Now, what it does is reverse sort the the list on the basis of first element
# of the nested list AND sort normally on the internal elements of the nested
# sorted list i.e
#
# first 2,3,4,5 etc are considered for sorting the list in reverse order( -e[0]
# == -2,-3,-4...) and then we sort the elements on the basis of second element
# for internal sorting (e[1] == 'w', 'a', 'b'...)


sorted(xs.items(), key=lambda x: x[1])

# Or:

import operator

sorted(xs.items(), key=operator.itemgetter(1))

