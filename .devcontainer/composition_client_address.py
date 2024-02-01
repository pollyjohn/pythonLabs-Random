class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = [] 

    def insert_adress(self, street, number):
        self.addresses.append(Address(street, number))
        
    #method to insert address outside class
    def insert_external_address(self, address):
        self.addresses.append(address)

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)
    
    def __del__(self):
        print('APAGANDO, ', self.name)

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print('APAGANDO, ', self.street, self.number)

    
client1 = Client('Icaro')
client1.insert_adress('manhatan','1242')
client1.insert_adress('washigton','1')
external_address = Address('Av Hope', 1213)
client1.insert_external_address(external_address)
client1.list_addresses()

del client1


print(external_address.street, external_address.number)
print('######################## here the code ends')



        