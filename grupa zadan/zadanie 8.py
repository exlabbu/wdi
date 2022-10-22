from random import Random
import random


def inuptValue():
    while True:
        try:
            a = int(input("Podaj liczbę całkowitą nieujemną do choinki "))                
        except:
            print("błędna wartość")
            continue
        else:
            if (a <= 0):
                continue
            break
    return a

def doXmasTree(a):
    i = 0
    l = 1
    for x in range(2,a-1):
        l+=2
    print(l)
    j = 1
    tab = "\t"
    while(j == ((l-1)/2)):
        tab = str(tab)+" \t"
        j+=1
    print(tab+"X")
    while(i != a):
        
        random.randint(2,a-1)

        # Dopisać resztę choinki!

doXmasTree(5)