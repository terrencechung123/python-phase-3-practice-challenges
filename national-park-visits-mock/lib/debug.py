#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker
import ipdb

from classes.customer import Customer
from classes.restaurant import Restaurant
from classes.review import Review

if __name__ == '__main__':
    fake = Faker()

    # customers = [Customer(fake.first_name(), fake.last_name()) for i in range(50)]
    # restaurants = [Restaurant(f"{fake.first_name()}'s") for i in range(25)]
    # reviews = [Review(rc(customers), rc(restaurants), randint(1, 5)) for i in range(200)]

    emiley = Customer("Emiley", "Palmquist")
    conner = Customer("Conner", "Palmer")
    red_robin = Restaurant("Red Robin")
    olive_garden = Restaurant("Olive Garden")

    review_1 = Review(emiley, red_robin, 5)
    review_2 = Review(emiley, red_robin, 4)
    review_3 = Review(conner, red_robin, 4)
    review_4 = Review(emiley, olive_garden, 4)

    # for review in olive_garden.reviews():
    #     print(review.restaurant.name)

    for customer in red_robin.customers():
        print(customer.get_full_name())

    ipdb.set_trace()
