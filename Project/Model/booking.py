from neo4j import GraphDatabase
from Model.car import findCarByCarid, updateCar
from Model.customer import findCustomerByname, customerBooking, customerRental

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")
