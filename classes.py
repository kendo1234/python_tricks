import datetime


class User:
    """Class to create a user. With a functions to initialize the class, this is called whenever you create a new instance of the class.
'self' is an argument that refers to the new object being created. The age function calculates the age for user based on the date attribute passed in"""


def __init__(self, full_name, birthday):
    # Store the values in a field
    self.name = full_name
    self.birthday = birthday

    # Extract first and last namea
    name_pieces = full_name.split(" ")  # pieces will be stored in an array
    self.first_name = name_pieces[0]
    self.last_name = name_pieces[-1]


def age(self):
    """Return the age of a user in years"""
    today = datetime.date(2001, 5, 12)
    yyyy = int(self.birthday[0:4])
    mm = int(self.birthday[4:6])
    dd = int(self.birthday[6:8])
    dob = datetime.date(yyyy, mm, dd)  # date of birth
    age_in_days = (today - dob).days
    age_in_years = age_in_days / 365
    return int(age_in_years)


user1 = User("Eric Idle", "19710315")  # instance of class or 'object'
print(user1.age())
