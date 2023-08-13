class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
        else:
            raise TypeError("Can't subtract Item from {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other
        else:
            raise TypeError("Can't subtract Item from {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.weight * other.weight
        elif isinstance(other, int):
            return self.weight * other
        else:
            raise TypeError("Can't multiply Item by {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.weight / other.weight
        elif isinstance(other, int):
            return self.weight / other
        else:
            raise TypeError("Can't divide Item by {}".format(type(other)))


item_1 = Item('Видиокарта', 15000, 0.8)
item_2 = Item('Процессор', 12000, 0.3)
item_3 = item_1 - item_2
print(item_3)
item_3 = item_2 + 1000
print(item_3)
item_3 = item_1 / 10
print(item_3)
item_3 = item_2 * 4
print(item_3)
