
class Customer:
    def __init__(self, name):
        self.name = name

    def get_customer_name(self):
        return self._name
    def set_customer_name(self,name):
        if isinstance(name, str) and (0 < len(name) < 16):
            self._name = name
        else:
            raise Exception('name is not valid.')
    customer = property(get_customer_name, set_customer_name)

    def orders(self):
        from classes.order import Order
        orders_list=[]
        for order in Order.all:
            if order.customer == self:
                orders_list.append(order)
        return orders_list


    def coffees(self):
        coffees_ordered = []
        for order in self.orders():
            if not order.coffee in coffees_ordered:
                coffees_ordered.append(order.coffee)
        return coffees_ordered

    def create_order(self, coffee, price):
        from classes.order import Order
        new_order = Order(self, coffee, price)
