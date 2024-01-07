import csv
import random
from faker import Faker
import unidecode

fake = Faker('pt_BR')

def generate_sequential_id():
    for id in range(1, 14002):  # Generate sequential IDs from 1 to 14001
        yield id

def generate_unique_name(existing_names):
    while True:
        name = fake.first_name() + " " + fake.last_name()
        if name not in existing_names:
            return name

def generate_random_client(id_generator, existing_names):
    id = next(id_generator)
    name = generate_unique_name(existing_names)
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
    cpf = fake.cpf()
    email = unidecode.unidecode((name.replace(" ", ".") + "@example.com").lower())

    return [id, name, birthdate, cpf, email]

def write_to_csv(data):
    with open('clientes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

id_generator = generate_sequential_id()
existing_names = set()
for _ in range(14000):  # Generate 14000 clients
    client_data = generate_random_client(id_generator, existing_names)
    existing_names.add(client_data[1])
    write_to_csv(client_data)