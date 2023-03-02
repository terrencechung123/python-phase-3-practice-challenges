#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    print('')
    print('')
    print('')
    terrence = Customer('Terrence')
    mocha = Coffee('Mocha')
    my_order = Order(terrence, mocha, 5)

    ipdb.set_trace()




    # def orders(self):
    #     from classes.order import Order
    #     orders_list=[]
    #     for order in Order.all:
    #         if order.coffee == self:
    #             orders_list.append(order)
    #     return orders_list


    # def customers(self):
    #     customers_who_ordered = []
    #     for order in self.orders():
    #         if not order.customer in customers_who_ordered:
    #             customers_who_ordered.append(order.customer)
    #     return customers_who_ordered