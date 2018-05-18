import datetime


class User:
    """Class to create a user. With a function to initialize the class, this is called whenever you create a new instance of the class.
'self' is an argument that refers to the new object being created. The age function calculates the age for a user based on the date attribute passed in"""

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
        today = datetime.datetime.now()
        dob = datetime.datetime.strptime(self.birthday, '%Y%m%d') # date of birth, strptime matches the regex value to the value passed into the call
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user1 = User("Eric Idle", "19850710")
print(user1.age())
