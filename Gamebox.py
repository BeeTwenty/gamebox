games = ["madlibs"]


def game_select():
    print("let's open a game:")
    print("games you can select are:")
    print(games)
    selection = input("select a game: ")
    print("Press 'q' to quit the program")
    if selection == "madlibs":
        madlibs()
    elif selection == "q":
        exit()
    else:
        game_select()


def madlibs():
    food = input("you're favorite food: ")
    name = input("Give me a name: ")
    adj = input("Give me an adjective: ")
    noun = input("Give me a noun: ")
    verb1 = input("Give me 3 verbs, verb 1: ")
    verb2 = input("verb 2: ")
    verb3 = input("verb 3: ")

    print(
        "It was %s day at school, and %s was super %s for lunch. But when she went outside to eat, a %s stole her %s! "
        "%s chased the %s all over school. She %s, %s, and %s through the playground. Then she tripped on her %s and "
        "the %s escaped! Luckily, %s’s friends were willing to share their %s with her." % (food, name, adj, noun,
                                                                                            food, name, noun, verb1,
                                                                                            verb2, verb3, noun, noun,
                                                                                            name, food))
    game_select()


print("Hello Welcome!")

print("Who are you?")
uname = input("name: ")
age = int(input("how old are you? "))
city = input("what city do you live in? ")
county = input("and what county is that in? ")

print(" so your name is %s and you are %s years old. you live in %s city wich is in %s  " % (uname, age, city, county))

game_select()
