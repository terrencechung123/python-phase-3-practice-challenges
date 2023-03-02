
class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        self.rating = rating
        self.customer = customer
        self.restaurant = restaurant
        Review.all.append(self)
        # Review.add_review_to_all(self)

    @classmethod
    def add_review_to_all(cls, review):
        cls.all.append(review)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if isinstance(rating, int) and (1 <= rating <= 5):
            self._rating = rating
        else:
            raise Exception(
                "rating not a number or less than 1 or greater than 5.")

    rating = property(get_rating, set_rating)

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("not an instance of Customer class")

    customer = property(get_customer, set_customer)

    def get_restaurant(self):
        return self._restaurant

    def set_restaurant(self, restaurant):
        from classes.restaurant import Restaurant
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            raise Exception("not an instance of Restaurant class")

    restaurant = property(get_restaurant, set_restaurant)

    # def add_customer_to_restaurant(self):
    #     pass

    # def add_review_to_restaurant(self):
    #     pass

    # def add_restaurant_to_customer(self):
    #     pass

    # def add_review_to_customer(self):
    #     pass
