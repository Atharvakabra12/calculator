import re

data = 0
run = True

def maths():
    global run
    global data

    equation = ""
    if data == 0:
        equation = input("ENTER NUMBERS : \n")
    else:
        equation = input(str(data))

    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,@:()]', '', equation)        #extract out only number

        if data == 0:
            data = eval(equation)
        else:
            data = eval(str(data) + equation)

while run:
    maths()
