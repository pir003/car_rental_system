from neo4j import GraphDatabase, Driver
from Project.Model.car import find_car_by_carid, update_car
from Project.Model.customer import find_customer_by_name, customer_booking, customer_rental
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


    

        
    # Metode for bestille bil
def order_car( name, car_id):
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
    update_car(car["car_id"], car["make"], car["model"], car["year"], car["location"], status="booked")
        
    # Opprette booking-relasjonen mellom kunden og bilen
    # Se om man må endre fra c til c_customer og c til c_car for å forhindre forvirring
    with _get_connection().session() as session:
        session.run(
            "MATCH (u:Customer {name: $name}) " 
            "MATCH (c:Car {car_id: $car_id}) "
            "WITH u, c " 
            "CREATE (u)-[:BOOKED]->(c) ",
            name=name, car_id=car_id
        )
        
        return {"success": True, "message": "Du har booket bilen!"}


        
# Metode for å kansellere en booking    
def cancel_car_order(name, car_id):
    #Sjekke om kunden har en booking i systemet
    if not customer_booking(name):
        return {"success": False, "error": "Du har ingen booking å kansellere"}
        
    #Sjekke om statusen på bilen er "booked"
    car_list = find_car_by_carid(car_id)
    if not car_list:
        return {"success": False, "error": "Car not found."}
        
    car = car_list[0]
    if car.get("status") != "booked":
        return {"success": False, "error": "Car is not booked."}
        
    # Endre statusen til bilen til booked
    update_car(car ["car_id"], car["make"], car["model"], car["year"], car["location"], status="available")
   
    # Slette "booked"-relasjonen mellom kunde og bil, og oppdatere status på bil
    query = (
        "MATCH (u:Customer)-[r:BOOKED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE r"
        )
    with _get_connection().session() as session:
        session.run(query, name=name, car_id=car_id)

        
        return {"success": True, "message": "Bookingen cancelled"}
        
def rent_car(name, car_id):
    # Sjekke om kunden har booket bilen
    if not customer_booking(name):
        return {"success": False, "error": "Du har ikke booket denne bilen"}

    #Sjekke om statusen på bilen er "booked"
    car_list = find_car_by_carid(car_id)
    if not car_list:
        return {"success": False, "error": "Car not found."}
        
    car = car_list[0]
    if car.get("status") != "booked":
        return {"success": False, "error": "Car is not booked."}
        
    # Endre statusen til bilen til booked
    update_car(car ["car_id"], car["make"], car["model"], car["year"], car["location"], status="rented")

    query = (
        "MATCH (u:Customer)-[r:BOOKED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE r "
        "CREATE (u)-[rent:RENTED]->(c) "
        )
    with _get_connection().session() as session:
        session.run(query, name=name, car_id=car_id)

        return {"success": True, "message": "You have now rented this car."}

        
def return_car(name, car_id, status):
        
    #Sjekke om kunden har leid bilen
    with _get_connection.session() as session:
        rental_data = session.run(
            "MATCH (u:Customer)-[rent:RENTED]->(c:Car) "
            "WHERE u.name = $name AND c.car_id = $car_id "
            "RETURN c ", 
            name=name, car_id=car_id
            )
        
    if not rental_data:
        return {"success": False, "error": "Customer has not rented this car"}
        
    #Endre statusen på bilen
    new_status = "available" if status == "ok" else "damaged"
        
    #Oppdatere bilens status og slette "RENTED"-relasjonen
    query = (
        "MATCH (u:Customer)-[rent:RENTED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE rent "
        "SET c.status = $new_status "
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