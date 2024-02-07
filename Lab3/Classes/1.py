class string_manipulations:
    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

strings = string_manipulations()

strings.getString()

strings.printString()