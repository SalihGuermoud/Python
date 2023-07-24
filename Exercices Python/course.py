from robot import *

n = 2

for n in range(1, 11):
    for loop in range(n):
        droite()
    ramasser()    
    for loop in range(n):
        gauche()
    deposer()    
