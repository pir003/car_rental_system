from neo4j import GraphDatabase, Driver
import json

# Creating a database connection:
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver


# Creating json nodes:
def node_to_json(node):
    if node is None:
        return {}
    else:
        node_properties = dict(node.items())
        return node_properties


# Creating a customer:
def save_customer (customer_id, name, age, address):
    with _get_connection().session() as session:
        customers = session.run(
            "MERGE (u:Customer {customer_id: $customer_id, name: $name, age: $age, address: $address}) "
            "RETURN u ",
            customer_id=customer_id, name = name, age = age, address = address
            )
        nodes_json = [node_to_json(record["u"]) for record in customers]
        return nodes_json


# Find a specific customer:
def find_customer_by_name(name):
    with _get_connection().session() as session:
        customers = session.run(
            "MATCH (u:Customer) "
            "WHERE u.name = $name "
            "RETURN u; ",
            name = name
            )
        nodes_json = [node_to_json(record["u"]) for record in customers]
        return nodes_json


# Find all customers:
def find_all_customers():
    with _get_connection().session() as session:
        customers = session.run(
            "MATCH (u:Customer) "
            "RETURN u; "
            )
        nodes_json = [node_to_json(record["u"]) for record in customers]
        return nodes_json


# Updating customer information:
def update_customer (customer_id, name, age, address):
    with _get_connection().session() as session:
        customers = session.run(
            "MATCH (u:Customer {customer_id: $customer_id}) "
            "SET u.name = $name, u.age = $age, u.address = $address "
            "RETURN u; ",
            customer_id=customer_id, name=name, age=age, address=address
            )
        nodes_json = [node_to_json(record["u"]) for record in customers]
        return nodes_json


# Deleting a customer:
def delete_customer (name):
    with _get_connection().session() as session:
        session.run(
            "MATCH (u:Customer {name: $name}) "
            "DELETE u; ",
            name = name
            )

# Booking a car:
def customer_booking(name):
    with _get_connection().session() as session:
        is_booked = session.run(
            "MATCH (u:Customer) - [:BOOKED]-> (car:Car) "
            "WHERE u.name = $name "
            "RETURN car ",
            name = name
            )
        booking = is_booked.single()
        return booking is not None


# Renting a car:
def customer_rental (name, car_id):
    with _get_connection().session() as session:
        is_rented = session.run(
            "MATCH (u:Customer) - [:RENTED]-> (car:Car) "
            "WHERE u.name = $name AND car.car_id = $car_id "
            "RETURN car ",
            name = name, car_id = car_id
            )
        rented = is_rented.single()
        return rented is not None


# Customer class:
class Customer:
    def __init__(self, customer_id ,name, age, address):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.address = address
    
    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self, value):
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
    
    def to_json(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "age": self.age,
            "address": self.address
        }