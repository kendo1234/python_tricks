import re

# Here we create a regex object using a raw string
# Use the search function to match the object and
# Print the resulting matched group (the regex in parenthesis forms a group)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Here there are 2 groups - note two sets of parenthesis
# Print each group and retrieve all by not specifying a group num
# calling groups retreives all groups, distinctly defined
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
# We can name the groups
areaCode, mainNumber = mo.groups()

# Pipe | can match multiple expressions
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

# ? Marks an optional match
# Note how both Batman and Batwoman are valid matches
batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('The Adventures of Batman')
mo4 = batRegex.search('The Adventures of Batwoman')

# Looking at a modified version of the phone number
# This time with optional match
# Note the ? represents 'match zero or one group preceeding this ?'
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo5 = phoneRegex.search('My number is 415-555-4242')
mo6 = phoneRegex.search('My number is 555-4242')

# asterix means match zero or more
# Note in the two examples, wo is matched once in mo7 and 4 times in mo8
batRegex = re.compile(r'Bat(wo)*man')
mo7 = batRegex.search('The Adventures of Batman')
mo8 = batRegex.search('The Adventures of Batwowowowoman')

# + means match one or more
batRegex = re.compile(r'Bat(wo)+man')
mo9 = batRegex.search('The Adventures of Batwoman')
mo10 = batRegex.search('The Adventures of Batwowowowoman')

# Curly braces matches a specified number of repetition of the designated characters
haRegex = re.compile(r'(Ha){3}')
mo11 = haRegex.search('HaHaHa')

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
print(areaCode)
print(mainNumber)
print(mo1.group())
print(mo2.group())
print(mo3.group())
print(mo5.group())
print(mo6.group())
print(mo7.group())
print(mo8.group())
print(mo9.group())
print(mo10.group())
print(mo11.group())