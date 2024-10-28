from neo4j import GraphDatabase, Driver
from Model.neo import _get_connection
from Model.car import findCarByCarid, updateCar
from Model.customer import findCustomerByname, customerBooking, customerRental

# Oppsett av databaseforbindelsen
#URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
#AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

#def _get_connection() -> Driver:
    #driver = GraphDatabase.driver(URI, auth=AUTH)
    #driver.verify_connectivity()
    #return driver

class Booking:
    
    def __init__(self):
        selv.driver = _get_connection()
        
    # Metode for bestille bil
    # Sjekke om kunden har en booking inne, sjekke om bilen er tilgjengelig
    # Opprette en booking-relasjon i databasen
    
    # Metode for å avbestille en bestilling
    # Sjekke om kunden har en booking i systemet + avbestille booking
    
    # Metode for å leie en bil
    # Sjekke om kunden har en booking i systemet + endre statusen til bilen fra booked til rented
    
    # Metode for å returnere en bil
    # Sjekke om kunden har leid den bilen
    # Status på bilen er en av parametrene + oppdatere statusen på bilen