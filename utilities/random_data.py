from faker import Faker
import random

class randomData:

    def __init__(self):
        self.faker = Faker()

    def firstName(self):
        return self.faker.first_name()

    def lastName(self):
        return self.faker.last_name()

    def email(self):
        return self.faker.email()

    def zip_code(self):
        return self.faker.zipcode()

    def mobile_number(self):
        return self.faker.numerify(text="##########")

