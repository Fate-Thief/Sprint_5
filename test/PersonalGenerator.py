from faker import Faker

faker = Faker()

class PersonalGenerator:
    random_email = faker.email()
    random_password = faker.password(length=6)


cls = PersonalGenerator()
print(cls.random_email)
print(cls.random_password)
