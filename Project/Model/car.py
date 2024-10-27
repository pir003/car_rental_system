from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def findCarByCarid(car_id):
    data = _get_connection().execute_query("MATCH (c:Car) where c.car_id = $car_id RETURN c;", car_id=car_id)
    if len(data[0]) > 0:
        car = Car (car_id, data[0] [0] [0]['make', 'model', 'year', 'location', 'status'])
        return car
    else:
        return Car (car_id, "Not found in DB")

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