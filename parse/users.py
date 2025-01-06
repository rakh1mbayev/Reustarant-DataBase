import json
import random
from faker import Faker

# For data generation
fake = Faker()

# users limit
num_users = 800

users = []

# Users generation
for i in range(1, num_users + 1):
    user = {
        "_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),  # Заменяем новую строку на запятую для читаемости
        "phone": fake.phone_number()
    }
    users.append(user)

# Saving in JSON
with open("random_users.json", "w") as file:
    json.dump({"users": users}, file, indent=4)

print("JSON файл сгенерирован и сохранен как random_users.json")
