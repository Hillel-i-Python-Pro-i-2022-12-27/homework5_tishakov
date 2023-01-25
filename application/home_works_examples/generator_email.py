from faker import Faker

fake = Faker(["en_US"])


def generator_email():
    data = []
    for _ in range(0, 100):
        data.append(fake.email())
    return data
