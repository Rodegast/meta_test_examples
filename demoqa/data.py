import os
from dsl import *
from faker import Faker

fake = Faker("ru_RU")

data = SCOPE("data")
data.фио     = fake.name()
data.email   = fake.email()
data.адрес1  = fake.address()
data.адрес2  = fake.address()
data.фамилия = fake.last_name()
data.имя     = fake.first_name()

data.mobile     = "1234567890"
data.address    = fake.address()
data.image      = os.path.join(CONFIG.TEST_CONFIG_PATH, "data", "kote.jpg")
data.image_name = "kote.jpg"

