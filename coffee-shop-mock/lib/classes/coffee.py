# from classes.customer import Customer

class Coffee:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception('name is not valid.')

    def get_coffee_name(self):
        return self._name
    def set_coffee_name(self, name):
        raise Exception('coffee name cannot be changed')
    name = property(get_coffee_name,set_coffee_name)

    def orders(self):
        from classes.order import Order
        orders_list=[]
        for order in Order.all:
            if order.coffee == self:
                orders_list.append(order)
        return orders_list


    def customers(self):
        customers_who_ordered = []
        for order in self.orders():
            if not order.customer in customers_who_ordered:
                customers_who_ordered.append(order.customer)
        return customers_who_ordered

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        price = [order.price for order in orders]
        num_orders = len(orders)
        sum_price = sum(price)
        return sum_price / num_orders