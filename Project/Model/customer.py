from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

# Creating a customer
def createCustomer (customer_id, name, age, address):
    _get_connection().execute_query(""" CREATE (c:Customer {customer_id: $customer_id, name: $name, age: $age, address: $address})""", customer_id = customer_id, name = name, age = age, address = address)

# Reading a customer
def findCustomerByname(customer_id):
    data = _get_connection().execute_query("MATCH (c:Customer) where c.customer_id = $customer_id RETURN c", customer_id = customer_id)
    if len(data[0]) > 0:
        customer = Customer (customer_id, data [0] [0] ['name'], data[0] [0] ['age'], data[0] [0]['address'])
        return customer
    else:
        return Customer (customer_id, "Not found in DB")

# Updating customer information
def updateCustomer (customer_id, name=None, age=None, address=None):
    updates = []
    if name is not None:
        updates.append ("c.name = $age")
    if age is not None:
        updates.append("c.age = $age")
    if address is not None:
        updates.append("c.address =$address")
    database_update = ", ".join(updates)
    query = f"MATCH (c.Customer) where c.customer_id = $customer_id SET {database_update}"
    _get_connection().execute_query(query, customer_id = customer_id, name = name, age = age, address = address)

#Deleting a customer
def deleteCustomer (customer_id):
    _get_connection().execute_query("MATCH (c.Customer) where c.customer_id = $customer_id DELETE c", customer_id = customer_id)

def checkCustomerBooking(customer_id):
    _get_connection().execute_query("MATCH (c.Customer) - [:BOOKED]->(car:Car) where c.customer_id =$customer_id RETURN car", customer_id = customer_id)


class Customer:
    def __init__(self, customer_id, name, age, address):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.address = address
    
    def get_Customerid(self):
        return self.customer_id
    
    def set_Customerid(self, value):
        self.customer_id = value
    
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