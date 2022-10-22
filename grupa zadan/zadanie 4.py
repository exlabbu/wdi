import re

class Human:

    name = "Domink"
    surName = "Motyl"
    age = 20
    favAnimal = "Pies"
    favDish = "Pizza"      

    def setValues(self):
        while True:
            name = input("Proszę podaj swoje imie: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ'-]+$",name))):
                self.name = name
                break
            print("błędna wartość")
        while True:
            surName = input("Proszę podaj swoje nazwisko: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ' -.]+$",surName))):
                self.surName = surName
                break
            print("błędna wartość")
        while True:
            try:
                self.age = int(input("Proszę podaj swój wiek: "))
            except ValueError:
                print("błędna wartość")
                continue
            else:
                break
        while True:
            favAnimal = input("Proszę podaj swoje ulubione zwierze: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ]+$",favAnimal))):
                self.favAnimal = favAnimal
                break
            print("błędna wartość")
        while True:
            favDish = input("Proszę podaj swoją ulubioną potrawę: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ]+$",favDish))):
                self.favDish = favDish
                break
            print("błędna wartość")


    def printIntroduction(self):
        print(" -- Parametry Człowieka -- ")
        print("Imie: "+self.name)
        print("Nazwisko: "+self.surName)
        print("Wiek: "+str(self.age))
        print("Ulubione Zwierze: "+self.favAnimal)
        print("Ulubiona Potrawa: "+self.favDish)

    def __init__(self):
        self.printIntroduction()
        decide=input("Czy chcesz zmienić powyższe wartości? Y/N ")
        if(bool(re.match("^[YyNnTt]$",decide))):
            if(decide != "N" and decide != "n"):
                self.setValues()
                self.printIntroduction()

    def doMath(self,a,b,r):
        try:
            w = a/b
        except:
            print("błędne wartości w dzieleniu")
        else:
            match r:
                case 0:
                    print(w)
                case 1:
                    print(round(w,1))
                case 3:
                    print(round(w,3))
                case 5:
                    print(round(w,5))
                case 10:
                    print(round(w,10))
obj = Human()

print(" -- Dzielenie 5 przez 7 -- ")
print(" bez zaokrąglenia ")
obj.doMath(5,7,0)
print(" zaokrąglenie do 1 miejsca po przecinku ")
obj.doMath(5,7,1)
print(" zaokrąglenie do 3 miejsc po przecinku ")
obj.doMath(5,7,3)
print(" zaokrąglenie do 5 miejsc po przecinku ")
obj.doMath(5,7,5)
print(" zaokrąglenie do 10 miejsc po przecinku ")
obj.doMath(5,7,10)

