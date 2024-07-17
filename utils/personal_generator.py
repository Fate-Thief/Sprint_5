from faker import Faker

faker = Faker()


class PersonalGenerator:
    username = "Nastia"
    random_email = faker.email()
    random_password = faker.password(length=6)


cls = PersonalGenerator()
