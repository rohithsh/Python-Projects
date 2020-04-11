import re

print("Equation Calculator")
print("Type 'quit' to exit")

pre=0;
run=True;

def calc():
    global run
    global pre
    eqn=""
    if pre==0:
        eqn=input("Eneter an Equation: ")
    else:
        eqn=input(str(pre))   #print previous equation & get set eqn=prev

    if eqn=='quit':
        print("Bye,Have a good day.")
        run=False
    else:
        eqn=re.sub('[a-zA-Z{}[]()!@,.?:;]','',eqn)
        if pre==0:
            pre=eval(eqn)
        else:
            pre=eval(str(pre)+eqn)


while run:
    calc()
