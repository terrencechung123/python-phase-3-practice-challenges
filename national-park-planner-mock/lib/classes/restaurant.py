

class Restaurant:
    all = []

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Name is not a string")

        Restaurant.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        raise Exception("Name cannot be changed")

    name = property(get_name, set_name)

    def reviews(self):
        from classes.review import Review
        restaurants_reviews = []
        for review in Review.all:
            if review.restaurant == self:
                restaurants_reviews.append(review)
        return restaurants_reviews

    def customers(self):
        customers_who_reviewed = []
        for review in self.reviews():
            if not review.customer in customers_who_reviewed:
                customers_who_reviewed.append(review.customer)
        return customers_who_reviewed

    def get_average_rating(self):
        pass

    @classmethod
    def get_all_restaurants(cls):
        pass
