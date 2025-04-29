class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value
    
    def decrement(self):
        self.value -= 1
        return self.value


num_1 = Counter(15)
num_2 = Counter(4)

print(f"первое число: {num_1.value}, первое число + 1: {num_1.increment()}\nвторое число: {num_2.value}, второе число + 1: {num_2.increment()}")
print(f"первое число: {num_1.value}, первое число - 1: {num_1.decrement()}\nвторое число: {num_2.value}, второе число - 1: {num_2.decrement()}")