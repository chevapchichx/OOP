import math

class Calculator:
    def add(self, num_1, num_2):
        return num_1 + num_2

    def sub(self, num_1, num_2):
        return num_1 - num_2
    
    def multi(self, num_1, num_2):
        return num_1 * num_2
    
    def div(self, num_1, num_2):
        if num_2 == 0:
            return("делить на 0 нельзя!!")
        return num_1 / num_2
    
    def sqrt(self, num_1):
        return math.sqrt(num_1)


calculator = Calculator()

print(f"cложение: {calculator.add(15, 4)}")
print(f"вычитание: {calculator.sub(15, 4)}")
print(f"умножение: {calculator.multi(15, 4)}")
print(f"деление: {calculator.div(15, 4)}")
print(f"квадратный корень: {calculator.sqrt(15)}")