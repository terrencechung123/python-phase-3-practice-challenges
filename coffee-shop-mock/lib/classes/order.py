class Order:
    all= []
    def __init__(self, customer, coffee, price):
        if isinstance(price, int or float):
            self._price = price
            self._customer = customer
            self._coffee = coffee
        else:
            raise Exception('order is not valid.')
        Order.get_all_orders(self)
    @classmethod
    def get_all_orders(cls, order):
        cls.all.append(order)

    def get_price(self):
        return self._price
    def set_price(self, price):
        if (0<price<11):
            self._price = price
        else:
            raise Exception('price must be a number between 1 and 10, inclusive.')
    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer,Customer):
            self._customer = customer
        else:
            raise Exception('this is not a valid instance of customer.')
    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception('this is not a valid instance of coffee.')
    coffee = property(get_coffee,set_coffee)