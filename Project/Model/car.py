from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

# Creating a car
def createCar (car_id, make, model, year, location, status="available"):
    _get_connection().execute_query(""" CREATE (c:Car {car_id: $car_id, make: $make, model: $model, year = $year, location = $location, status = $status})""", car_id = car_id, make = make, model = model, year = year, location = location, status = status)

# Reading a car
def findCarByCarid(car_id):
    data = _get_connection().execute_query("MATCH (c:Car) where c.car_id = $car_id RETURN c;", car_id=car_id)
    if len(data[0]) > 0:
        car = Car (car_id, data[0][0]['make'], data[0][0]['model'], data[0][0]['year'], data[0][0]['location'], data[0][0]['status'])
        return car
    else:
        return Car (car_id, "Not found in DB")

# Updating car information
def updateCar (car_id, make=None, model=None, year=None, location=None, status=None):
    updates = []
    if make is not None:
        updates.append("c.make = $make")
    if model is not None:
        updates.append("c.model =$model")
    if year is not None:
        updates.append("c.year = $year")
    if location is not None:
        updates.append("c.location = $location")
    if status is not None:
        updates.append("c.status = $status")
    database_update = ", ".join(updates)
    query = f"MATCH (c.Car) where c.car_id = $car_id SET {database_update}"
    _get_connection().execute_query(query, car_id = car_id, make = make, maodel = model, yeaar = year, location = location, status = status)

#Deleting a car
def deleteCar (car_id):
    _get_connection().execute_query("MATCH (c.Car) where c.car_id = $car_id DELETE c", car_id = car_id)

class Car:
    def __init__(self, car_id, make, model, year, location, status = "available"):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.locatiton = location
        self.status = status

    
    def get_Status (self):
        return self.status
    
    def set_Status (self, new_status):
        self.status = new_status