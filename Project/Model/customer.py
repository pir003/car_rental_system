from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def findCustomerByname(name):
    data = _get_connection().execute_query("MATCH (c:Customer) where c.name = $name RETURN c.age AS age, c.address AS address", name=name)
    if len(data[0]) > 0:
        customer = Customer (name, data[0] [0] [0] ['age', 'address'])
        return customer
    else:
        return Customer (name, "Not found in DB")

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def get_Name(self):
        return self.name
    
    def set_Name(self, value):
        self.name = value
    
    def get_Age(self):
        return self.age
    
    def set_Age(self, value):
        self.age = value
    
    def get_Address(self):
        return self.address
    
    def set_Address(self, value):
        self.address = value