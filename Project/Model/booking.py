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
        self.driver = _get_connection
        
    # Metode for bestille bil
    def order_car(self, customer_id, car_id):
        # Sjekke om kunden har en booking i systemet fra før av
        if customerBooking(customer_id):
            return {"error": "Customer have already booked a car"}
        
        # Sjekke om bilen er tilgjengelig eller ikke
        car = findCarByCarid(car_id)
        if car.get_Status() != "available":
            return {"error": "Car is not available."}
        
        # Endre statusen til bilen til booked
        updateCar(car_id, status="booked")
        
        # Opprette booking-relasjonen mellom kunden og bilen
        # Se om man må endre fra c til c_customer og c til c_car for å forhindre forvirring
        query = ("MATCH (c:customer), (c:Car)"
                 "WHERE c.customer_id = $customer_id AND c.car_id = $car_id"
                 "CREATE (c)-[:BOOKED]->(c)")
        self.driver().execute_query(query, customer_id=customer_id, car_id=car_id)
        return {"Success": "Du har booket bilen!"}
        
    # Metode for å kansellere en booking    
    def cancel_car_order(self, customer_id, car_id):
        # Sjekke om kunden har en booking i systemet
        if not customerBooking(customer_id):
            return {"Error": "Du har ingen booking å kansellere"}
        
        # Sjekke om statusen på bilen er "booked"
        car = findCarByCarid(car_id)
        if car.get_Status() != "booked":
            return {"error": "Bilen er ikke booket"}
        
        # Slette "booked"-relasjonen mellom kunde og bil, og oppdatere status på bil
        query = ("MATCH (c:Customer)-[r:BOOKED]->(c:Car)"
                 "WHERE c.customer_id = $customer_id AND c.car_id = $car_id"
                 "DELETE r")
        
        self.driver().execute_query(query, customer_id=customer_id, car_id=car_id)
        updateCar(car_id, status="available")
        
        return {"success": "Bookingen er kansellert"}
        
    def rent_car(self, customer_id, car_id):
        # Sjekke om kunden har booket bilen
        if not customerBooking(customer_id):
            return {"error": "Du har ikke booket denne bilen"}
        
        query = ("MATCH (c:Customer)-[r:BOOKED]->(c:Car)"
                 "WHERE c.customer_id = $customer_id AND c.car_id = $car_id"
                 "DELETE r"
                 "CREATE (c)-[r:RENTED]->(c)")
        
        self.driver().execute_query(query, customer_id=customer_id, car_id=car_id)
        updateCar(car_id, status="rented")
        
        
     
    # Sjekke om kunden har en booking inne, sjekke om bilen er tilgjengelig
    # Opprette en booking-relasjon i databasen
    
    # Metode for å avbestille en bestilling
    # Sjekke om kunden har en booking i systemet + avbestille booking
    
    # Metode for å leie en bil
    # Sjekke om kunden har en booking i systemet + endre statusen til bilen fra booked til rented
    
    # Metode for å returnere en bil
    # Sjekke om kunden har leid den bilen
    # Status på bilen er en av parametrene + oppdatere statusen på bilen