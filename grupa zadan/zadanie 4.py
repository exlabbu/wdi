import re

class Human:

    def __init__(self):
        while True:
            name = input("Proszę podaj swoje imie: ")
            try:
                # problem jest w tym że tu nie chce on realnie stosować się do wyjątków
                # nw czy ta konstrukcja nie jest trochę problemem, trzeba ją zdebugować
                state = bool(re.match("[A-Za-zżńóąśćłźŹŚ]",name))
            except ValueError:
                print("flag error name Human")
                continue
            else:
                print("flag break name Human")
                self.name = name
                break
        SurName = input("Proszę podaj swoje nazwisko: ")
        #to jedyne w pełni działa i nie pozwala wprowadzić innego wejścia niż int
        while True:
            try:
                self.Age = int(input("Proszę podaj swój wiek: "))
            except ValueError:
                print("flag error age Human")
                continue
            else:
                print("flag break age Human")
                break
        FavAnimal = input("Proszę podaj swoje ulubione zwierze: ")
        FavDish = input("Proszę podaj swoją ulubioną potrawę: ")


    def printName(self):
        print(self.name)
    def printSurName(self):
        print(self.SurName)
    def printAge(self):
        print(self.Age)
    def printFavAnimal(self):
        print(self.FavAnimal)
    def printFavDish(self):
        print(self.FavDish)
    def doMath(a,b):
        print(a/b)

obj = Human()
        
