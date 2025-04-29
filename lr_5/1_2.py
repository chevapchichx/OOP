class Product:
    def __init__(self, calories, weight):
        self.calories = float(calories)
        self.weight = float(weight)
    
    def __copy__(self):
        return Product(self.calories, self.weight)
    
    def __str__(self):
        return f"{self.calories} calories in 100 g, weight {self.weight}g"
    
    def get_total_calories(self):
        return (self.calories * self.weight) / 100


class Vitamin(Product):
    def __init__(self, calories, weight, vitamin_c_per_g):
        super().__init__(calories, weight)
        self.vitamin_c_per_g = float(vitamin_c_per_g)

    def get_total_amount_vitamin_c_in_product(self):
        return self.weight * self.vitamin_c_per_g


milk = Vitamin(30, 500, 0.04)
print(milk.__copy__())
print(milk.get_total_calories())
print(milk.get_total_amount_vitamin_c_in_product())
