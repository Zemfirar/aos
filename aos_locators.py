from faker import Faker


fake = Faker(locale='en_CA')

AOS_URL = 'https://advantageonlineshopping.com/'
AOS_TITLE = ' Advantage Shopping'

# new_username = fake.user_name()
# new_password = fake.password()
email = fake.email()
# new_first_name = fake.first_name()
# new_last_name = fake.last_name()
# new_full_name = f'{new_first_name} {new_last_name}'

contact_us_subject = fake.sentence(nb_words=5)


def get_new_user():
    return fake.user_name(), fake.password(), fake.email(), fake.first_name(), fake.last_name()


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"
