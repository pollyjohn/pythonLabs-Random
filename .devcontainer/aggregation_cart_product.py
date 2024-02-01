class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])
    
    def insert_products(self, *products):
        #self._products.extend(products)
        #self._products += products
        for product in products:
            self._products.append(product)

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()

class Product:
    def __init__(self, name, price):
        self.price = price
        self.name = name

cart = Cart()
p1, p2 = Product('pen', 1.20), Product('shirt', 20)
cart.insert_products(p1, p2)
cart.list_products()
print('total:', cart.total())
