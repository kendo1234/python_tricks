# A tuple is a sequence of immutable Python objects. Tuples are sequences, just
# like lists. The differences between tuples and lists are, the tuples cannot be
# changed unlike lists and tuples use parentheses, whereas lists use square
# brackets.
# Tuples are immutable which means you cannot update or change the values of
# tuple elements.
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new car class works as expected

my_car = Car('red', 3812.4)

# Like tuples, namedtuples are immutable:
# >>> my_car.color = 'blue'
# AttributeError: "can't set attribute"


print(my_car)