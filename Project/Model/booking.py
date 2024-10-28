from neo4j import GraphDatabase, Driver
from Model.car import findCarByCarid, updateCar
from Model.customer import findCustomerByname, customerBooking, customerRental

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver