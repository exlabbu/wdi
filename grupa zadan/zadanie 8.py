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
            elif(a == 1):
                print("X")
                print("U")
                exit()
            break
    return a

class XmasTree:

    def __init__(self,a):
        # a-1 to odległość jaką mam do pnia z lewej strony
        self.toTheTrunk = a-1
        self.height = a

    def countSapce(self,lev):
        # przyjmuje że level to aktualny poziom liczony od 1
        s = ""
        for x in range(1,self.toTheTrunk - (lev-1)):
            s = s + " "
        return s

    def setStarOnTheTop(self):
        print(self.countSapce(1)+"X")

    def makeStandUnderTree(self):
        print(self.countSapce(1)+"U")

    def makeTreeWithXmasTreeBaubles(self, lev):
        # parametrem jest level początkowy
        def countXmasWidth(lev):
            def randomizeTreeBoubles(b):
                s = ""
                i = 0
                while(i != b):
                    if(random.randint(0,b*2) == 0):
                        s = s + "o"
                    else:
                        s = s + "*"
                    i+=1
                return s


            s = randomizeTreeBoubles(3)
            for x in range(1,lev-1):
                s = s + randomizeTreeBoubles(2)
            return s
        while (lev != self.height):
            print(self.countSapce(lev)+countXmasWidth(lev))
            lev += 1

    def setTree(self):
        self.setStarOnTheTop()
        self.makeTreeWithXmasTreeBaubles(2)
        self.makeStandUnderTree()



    
    

obj = XmasTree(inuptValue())
obj.setTree()