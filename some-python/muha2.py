class FizzBuzz:
    def __init__(self):
        self.control()

    def findDef(self, i):
        if i % self.common_num == 0:
            return i
        elif i % self.num1 == 0:
            return '*'
        elif i % self.num2 == 0:
            return '#'
        else:
            return i

    def inputNumbers(self):
        self.max_num = int(input("Enter a maximum number: "))
        self.num1 = int(input("Enter a num1: "))
        self.num2 = int(input("Enter a num2: "))
        self.common_num = self.num1 * self.num2
        self.control()

    def outputNumbers(self):    
        self.line_feed = int(input("The line feed: "))
        for i in range(1, self.max_num + 1):
            cell = self.findDef(i)
            print('{:>2}'.format(cell), end = " ")
            if i % self.line_feed == 0:
                print("")
        print("")
        self.control()

    def control(self):
        action = input("Enter command (i, d, e): ")
        if action == 'i':
            self.inputNumbers()
        elif action == 'd':
            self.outputNumbers()
        elif action == 'e':
            print("Program is done")
        else:
            print("Wrong commands. i, d, or, e!")
            self.control()

FizzBuzz = FizzBuzz()