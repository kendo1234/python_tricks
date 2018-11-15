def kilograms_to_pounds():
    name = str((input("Hi, what is your name? : ")))
    kilo = int(input(f"Hello {name}, please enter a value in kilograms : "))
    pounds = kilo * 2.2
    print(f"Ok {name}, {kilo}kg in pounds is {pounds}, if this is your weight then maybe put down the fork?")


kilograms_to_pounds()
