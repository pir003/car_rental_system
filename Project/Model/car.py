from neo4j import GraphDatabase, Driver
import json

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    if node is None:
        return {}
    else:
        node_properties = dict(node.items())
        return node_properties

# Creating a car
def save_car (car_id, make, model, year, location, status="available"):
    with _get_connection().session() as session:
        cars = session.run(
            "MERGE (c:Car {car_id: $car_id, make: $make, model: $model, year: $year, location: $location, status: $status}) "
            "RETURN c ",
            car_id = car_id, make = make, model = model, year = year, location = location, status = status
            )
        nodes_json = [node_to_json(record["c"]) for record in cars]
        return nodes_json

# Find a specific car
def find_car_by_carid(car_id):
    with _get_connection().session() as session:
        cars = session.run(
            "MATCH (c:Car) "
            "WHERE c.car_id = $car_id "
            "RETURN c ",
            car_id = car_id
            )
        nodes_json = [node_to_json(record["c"]) for record in cars]
        return nodes_json

# Find all cars
def find_all_cars():
    with _get_connection().session() as session:
        cars = session.run(
            "MATCH (c:Car) "
            "RETURN c; "
            )
        nodes_json = [node_to_json(record["c"]) for record in cars]
        print (nodes_json)
        return nodes_json

# Updating car information
def update_car (car_id, make, model, year, location, status):
    with _get_connection().session() as session:
        cars = session.run(
            "MATCH (c:Car {car_id: $car_id}) "
            "SET c.make = $make, c.model = $model, c.year = $year, c.location = $location, c.status = $status "
            "RETURN c; ",
            car_id = car_id, make = make, model = model, year = year, location = location, status = status
            )
        print (cars)
        nodes_json = [node_to_json(record["c"]) for record in cars]
        print (nodes_json)
        return nodes_json
    


#Deleting a car
def delete_car (car_id):
    with _get_connection().session() as session:
        session.run(
            "MATCH (c:Car {car_id: $car_id}) "
            "DELETE c; ",
            car_id = car_id
            )

class Car:
    def __init__(self, car_id, make, model, year, location, status= "available"):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = status

    
    def get_status (self):
        return self.status
    
    def set_status (self, new_status):
        self.status = new_status

    def to_json(self):
        return {
            "car_id": self.car_id, 
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "location": self.location,
            "status": self.status
            }