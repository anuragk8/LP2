import random

name = "Bot Number 286"
monsoon = "rainy"
food = ["pizza", "fries"]
mood = "Smiley"
resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "My name is the {0}".format(name)],
    "what's today's weather?": [
        "The weather is {0}".format(monsoon),
        "It's {0} today".format(monsoon)],
    "how are you?": [
        "I am feeling {0}".format(mood),
        "{0}! How about you?".format(mood),
        "I am {0}! How about yourself?".format(mood), ],
    "": ["Hey! Are you there?",
         "What do you mean by these?",
         ],
    "what are the food options":
        ["food {0}".format(food)],
    "default": [
        "This is a default message"]}


def res(message):
    if message in resp:
        x = random.choice(resp[message])
    else:
        x = random.choice(resp["default"])
    return x


def real(xtext):
    if "name" in xtext:
        ytext = "what's your name?"
    elif "monsoon" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    elif "food" in xtext:
        ytext = "what are the food options"
    elif xtext == "":
        ytext = ""
    else:
        ytext = "default"
    return ytext


def send_message(message):
    print((message))
    response = res(message)
    print((response))


print("BOT: What is your name?")
user_name = input()
while 1:
    my_input = input("Enter your message: ")
    my_input = my_input.lower()
    if my_input == "exit" or my_input == "stop":
        break
    related_text = real(my_input)
    send_message(related_text)


