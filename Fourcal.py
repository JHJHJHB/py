class fourcal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        self.num1 = result
        return result
    def min(self):
        result = self.num1 - self.num2
        self.num1 = result
        return result
    def mul(self):
        result = self.num1 * self.num2
        self.num1 = result
        return result
    def div(self):
        result = self.num1 / self.num2
        self.num1 = result
        return result
    def reset(self):
        self.num1 = 0
        self.num2 = 0