"""An example of storing values in a list, as oppose to creating many single variables.
 The script stores each value entered in the console, to a list named cat_names and print the contents when stopped"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
