from neo4j import GraphDatabase, Driver
from Project.Model.car import find_car_by_carid, update_car
from Project.Model.customer import find_customer_by_name, customer_booking, customer_rental
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


# Method for ordering a car:
def order_car( name, car_id):
    # Checking if the customer has ordered a car previously:
    if customer_booking(name):
        return {"success": False, "error": "Customer have already booked a car"}
        
    # Checking if the car is available or not:
    car_list = find_car_by_carid(car_id)
    if not car_list:
        return {"success": False, "error": "Car not found."}
        
    car = car_list[0]
    if car.get("status") != "available":
        return {"success": False, "error": "Car is not available."}
        
    # Changing the car's status to booked:
    update_car(car["car_id"], car["make"], car["model"], car["year"], car["location"], status="booked")
        
    # Creating booking relations between customer and car: 
    with _get_connection().session() as session:
        session.run(
            "MATCH (u:Customer {name: $name}) " 
            "MATCH (c:Car {car_id: $car_id}) "
            "WITH u, c " 
            "CREATE (u)-[:BOOKED]->(c) ",
            name=name, car_id=car_id
        )
        
        return {"success": True, "message": "Car successfully booked!"}


# Method for cancelling a booking:   
def cancel_car_order(name, car_id):
    # Checks if the customer has a booking in the system already:
    if not customer_booking(name):
        return {"success": False, "error": " No booking found."}
        
    # Checks if the car is already booked:
    car_list = find_car_by_carid(car_id)
    if not car_list:
        return {"success": False, "error": "Car not found."}
        
    car = car_list[0]
    if car.get("status") != "booked":
        return {"success": False, "error": "Car is not booked."}
        
    # Changes the car's status to booked:
    update_car(car ["car_id"], car["make"], car["model"], car["year"], car["location"], status="available")
   
    # Deletes the booking relation between car and customer, and updates the car's status: 
    query = (
        "MATCH (u:Customer)-[r:BOOKED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE r"
        )
    with _get_connection().session() as session:
        session.run(query, name=name, car_id=car_id)
        
        return {"success": True, "message": "Booking cancelled"}


# Method for renting a car:        
def rent_car(name, car_id):
    # Checks if the customer has booked the car: 
    if not customer_booking(name):
        return {"success": False, "error": "No booking found"}

    # Checks if the car's status is booked: 
    car_list = find_car_by_carid(car_id)
    if not car_list:
        return {"success": False, "error": "Car not found."}
        
    car = car_list[0]
    if car.get("status") != "booked":
        return {"success": False, "error": "Car is not booked."}
        
    # Changes the status of the car to rented: 
    update_car(car ["car_id"], car["make"], car["model"], car["year"], car["location"], status="rented")

    query = (
        "MATCH (u:Customer)-[r:BOOKED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE r "
        "CREATE (u)-[rent:RENTED]->(c) "
        )
    with _get_connection().session() as session:
        session.run(query, name=name, car_id=car_id)

        return {"success": True, "message": "Car successfully rented."}


# Method for returning a car:        
def return_car(name, car_id, status):
        
    # Checks if the customer has rented the car:
    with _get_connection().session() as session:
        rental_data = session.run(
            "MATCH (u:Customer)-[rent:RENTED]->(c:Car) "
            "WHERE u.name = $name AND c.car_id = $car_id "
            "RETURN c ", 
            name=name, car_id=car_id
            )
        
    if not rental_data:
        return {"success": False, "error": "Customer has not rented this car"}
        
    # Changes the car's status: 
    new_status = "available" if status == "ok" else "damaged"
        
    # Updates the car's status and deletes the "rented" relationsship: 
    query = (
        "MATCH (u:Customer)-[rent:RENTED]->(c:Car) "
        "WHERE u.name = $name AND c.car_id = $car_id "
        "DELETE rent "
        "SET c.status = $new_status "
    )
    with _get_connection().session() as session:
        session.run(query, name=name, car_id=car_id, new_status=new_status)
        
    return {"success": True, "message": f"Car successfully returned; status: '{new_status}'"}
