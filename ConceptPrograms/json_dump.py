# The standard string repr (representation) function for dicts is hard to read
# the json module can do a much better, prettier version

import json

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

print(json.dumps(my_mapping, indent=4, sort_keys=True))

# Note this only works with dicts containing
# primitive types