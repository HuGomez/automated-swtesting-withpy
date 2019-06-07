# known_people = ["Charles", "Joan", "Max"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))


def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")

    people_without_spaces = [person.strip() for person in people_list]
    # for person in people_list:
    #     people_without_spaces.append(person.strip())

    return people_without_spaces


def ask_user():
    person = input("Enter the person you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))


# who_do_you_know()
ask_user()
