import random
import math
import sys
global varprint
varprint = False


line = 0
with open("D:/file/helloworld.jm", "r") as file:
    ee = file.readlines()
    for x in ee:
        line += 1
        if "PRINT: " in  x:
            print(x.replace("PRINT: ", "").strip())
            continue
        if "print: " in x:
            print("\n")
            print(f"Error in line {line}:")
            print(f"'print:' is incorrect. maybe you meant 'PRINT:'?")
            sys.exit()
        if "INPUT:" in x and not "SAVEINPUT: " in x:
            input()
            continue
        if "SAVEINPUT: " in x:
            varname = x.replace("SAVEINPUT: ", "").strip()
            exec(f"{varname} = input()", globals())
            continue
        if "PRINTSAVE: " in x:
            varprint = x.replace("PRINTSAVE: ", "")
            try:
                exec(f"print({varprint})")
            except:
                print(f"\nError in line {line}:")
                print(f"The variable \"{varprint}\" does not exist. You may have spelt the variable incorrectly.")