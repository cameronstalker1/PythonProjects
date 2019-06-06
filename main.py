'''
Project: Calculator
Author: Cameron 'the' Stalker

'''

import re

print("Magical Calculator")
print("Type 'q' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""

    # if there is a previous calculation, use this in the prompt
    if previous == 0:
        equation = input("Enter equation:\n")
    else:
        equation = input(str(previous))

    # if the user quits
    if equation == "q":
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', "", equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
