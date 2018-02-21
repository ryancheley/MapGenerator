

class City:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    @staticmethod
    def create_from_dict(lookup):
        return City(
            lookup['street'],
            lookup['city'],
            lookup['state'],
        )