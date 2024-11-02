from neo4j import GraphDatabase, Driver
from Project.Model.neo import _get_connection
from Project.Model.car import find_car_by_carid, update_car
from Project.Model.customer import find_customer_by_name, customer_booking, customer_rental
import json

# Oppsett av databaseforbindelsen
#URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
#AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

#def _get_connection() -> Driver:
    #driver = GraphDatabase.driver(URI, auth=AUTH)
    #driver.verify_connectivity()
    #return driver

def node_to_json(node):
    if node is None:
        return {}
    else:
        node_properties = dict(node.items())
        return node_properties

class Booking:
    
    def __init__(self):
        self.driver = _get_connection
        
    # Metode for bestille bil
    def order_car(self, name, car_id):
        # Sjekke om kunden har en booking i systemet fra før av
        if customer_booking(name):
            return {"success": False, "error": "Customer have already booked a car"}
        
        # Sjekke om bilen er tilgjengelig eller ikke
        car_list = find_car_by_carid(car_id)
        if not car_list:
            return {"success": False, "error": "Car not found."}
        
        car = car_list[0]
        if car.get("status") != "available":
            return {"success": False, "error": "Car is not available."}
        
        # Endre statusen til bilen til booked
        update_car(car_id, status="booked")
        
        # Opprette booking-relasjonen mellom kunden og bilen
        # Se om man må endre fra c til c_customer og c til c_car for å forhindre forvirring
        query = (
            "MATCH (u:Customer), (c:Car) "
            "WHERE u.name = $name AND c.car_id = $car_id "
            "CREATE (u)-[b:BOOKED]->(c) "
            "RETURN b"
            )
        
        print(f"Running query: {query} with parameters: name={name}, car_id={car_id}")
        
        with _get_connection().session() as session:
            session.run(query, name=name, car_id=car_id)
        return {"success": True, "message": "Du har booket bilen!"}
        
    # Metode for å kansellere en booking    
    def cancel_car_order(self, name, car_id):
        # Sjekke om kunden har en booking i systemet
        if not customer_booking(name):
            return {"success": False, "error": "Du har ingen booking å kansellere"}
        
        # Sjekke om statusen på bilen er "booked"
        car = find_car_by_carid(car_id)
        if car.get_status() != "booked":
            return {"success": False, "error": "Bilen er ikke booket"}
        
        # Slette "booked"-relasjonen mellom kunde og bil, og oppdatere status på bil
        query = (
            "MATCH (u:Customer)-[r:BOOKED]->(c:Car)"
            "WHERE u.name = $name AND c.car_id = $car_id"
            "DELETE r"
            )
        with _get_connection().session() as session:
            session.run(query, name=name, car_id=car_id)

        update_car(car_id, status="available")
        
        return {"success": True, "message": "Bookingen er kansellert"}
        
    def rent_car(self, name, car_id):
        # Sjekke om kunden har booket bilen
        if not customer_booking(name):
            return {"success": False, "error": "Du har ikke booket denne bilen"}
        
        query = (
            "MATCH (u:Customer)-[r:BOOKED]->(c:Car)"
            "WHERE u.name = $name AND c.car_id = $car_id"
            "DELETE r"
            "CREATE (u)-[r:RENTED]->(c)"
            )
        with _get_connection().session() as session:
            session.run(query, name=name, car_id=car_id)

        update_car(car_id, status="rented")
        
    def return_car(self, name, car_id, status):
        
        #Sjekke om kunden har leid bilen
        with _get_connection.session() as session:
            rental_data = session.run(
                "MATCH (u:Customer)-[r:RENTED]->(c:Car)"
                "WHERE u.name = $name AND c.car_id = $car_id"
                "RETURN c", 
                name=name, car_id=car_id
                )
        
        if not rental_data:
            return {"success": False, "error": "Customer has not rented this car"}
        
        #Endre statusen på bilen
        new_status = "available" if status == "ok" else "damaged"
        
        #Oppdatere bilens status og slette "RENTED"-relasjonen
        query = (
            "MATCH (u:Customer)-[r:RENTED]->(c:Car)"
            "WHERE u.name = $name AND c.car_id = $car_id"
            "DELETE r"
            "SET c.status = $new_status"
        )
        with _get_connection().session() as session:
            session.run(query, name=name, car_id=car_id, new_status=new_status)
        
        return {"success": True, "message": f"Bilen er returnert og statusen er '{new_status}'"}

        
     
    # Sjekke om kunden har en booking inne, sjekke om bilen er tilgjengelig
    # Opprette en booking-relasjon i databasen
    
    # Metode for å avbestille en bestilling
    # Sjekke om kunden har en booking i systemet + avbestille booking
    
    # Metode for å leie en bil
    # Sjekke om kunden har en booking i systemet + endre statusen til bilen fra booked til rented
    
    # Metode for å returnere en bil
    # Sjekke om kunden har leid den bilen
    # Status på bilen er en av parametrene + oppdatere statusen på bilen