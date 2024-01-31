from faker import Faker
import json
import random
file_path = 'json_dump.json'
fake = Faker()

class Pessoas:
    def __init__(self, name, age, instance_name) -> None:
        self.instance_name = instance_name
        self.name = name
        self.age = age

    def introduction(self):
        print(f'Hi! My name is {self.name}')

    @classmethod
    def criar_pessoa(cls, name, age, ps_name):
        return cls("anonimous", age, ps_name)


instances = []
# Creating objects 
for i in range(5):
    instance_name = f"P_{i}"
    instance = Pessoas(fake.name(), random.randint(0,100) , instance_name= instance_name) 
    instances.append(instance.__dict__)

# creating objects anonimously through classmethoud

for i in range(5):
    ps_name = f"ps_{i}"
    ps = Pessoas.criar_pessoa(fake.name(), random.randint(0,100), ps_name)
    print(vars(ps))
print(ps.name, ps.age)
def json_dump():
    with open(file_path, 'w') as file:
        json.dump(instances, file, ensure_ascii=False, indent=3)

            