from typing import List

my_string = "hold my beer"

for character in my_string: # iterables are strings, lists, sets, tuples and more
    print(character)

more_print = True
while more_print == True:
    print(10)

    user_input = input("should we print again? (y/n)")
    if user_input == 'n':
        more_print = False