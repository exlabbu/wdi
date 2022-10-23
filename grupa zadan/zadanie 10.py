class kalculator:
    lastResult = 0

    

    def addition(self, *args):
        sum = self.lastResult
        for x in args:
            sum += args[x]
        self.lastResult = sum

    def subtraction(self, *args):
        sub = self.lastResult
        for x in args:
            sub -= args[x]
        self.lastResult = sub

    def product(self, *args):
        prod = self.lastResult
        for x in args:
            prod *= args[x]
        self.lastResult = prod


    def quotient(self, *args):
        quot = self.lastResult
        for x in args:
            quot /= args[x]
        self.lastResult = quot


    def square(self, *args):

    def rootSquare(self, *args):
        