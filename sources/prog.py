"""
Un script python prenant 3 arguments dont le premier est l'opération voulue et les deux suivants 
les deux entiers 
"""

import calc 
import sys 

if len(sys.argv) - 1 != 3: 
    print("Vous n'avez pas entré 3 arguments.")
    sys.exit(0)

res = calc.ope(sys.argv[1],sys.argv[2],sys.argv[3])
if res != None: 
    print("{} {} {} = {}".format(sys.argv[2],sys.argv[1],sys.argv[3],res))
