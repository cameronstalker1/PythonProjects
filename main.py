import re

print("Magical Calculator")
print("Type 'q' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:\n")
    else:
        equation = input(str(previous))
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