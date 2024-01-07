import csv
import random
from faker import Faker
import unidecode

fake = Faker('pt_BR')

def generate_unique_id(existing_ids):
    while True:
        id = random.randint(1, 99999)
        if id not in existing_ids:
            return id

def generate_unique_name(existing_names):
    while True:
        name = fake.first_name() + " " + fake.last_name()
        if name not in existing_names:
            return name

def generate_random_client(existing_ids, existing_names):
    id = generate_unique_id(existing_ids)
    name = generate_unique_name(existing_names)
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
    cpf = fake.cpf()
    email = unidecode.unidecode((name.replace(" ", ".") + "@example.com").lower()) 

    return [id, name, birthdate, cpf, email]

def write_to_csv(data):
    with open('clientes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

existing_ids = set()
existing_names = set()
for _ in range(99999): 
    client_data = generate_random_client(existing_ids, existing_names)
    existing_ids.add(client_data[0])
    existing_names.add(client_data[1])
    write_to_csv(client_data)