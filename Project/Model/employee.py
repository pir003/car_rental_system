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

# Creating an employee
def save_employee (employee_id, name, address, branch):
    with _get_connection().session() as session:
        employees = session.run ("MERGE (e:Employee {employee_id: $employee_id, name: $name, address: $address, branch: $branch})"
                                 "RETURN e",
                                 employee_id = employee_id, name = name, address = address, branch = branch)
        nodes_json = [node_to_json(record["e"]) for record in employees]
        return nodes_json
    
# Find a specific employee:
def find_employee_by_id(employee_id):
    with _get_connection().session() as session:
        employees = session.run ("MATCH (e:Employee)",
                                 "WHERE e.employee_id = $employee_id"
                                 "RETURN e;",
                                 employee_id = employee_id)
        nodes_json = [node_to_json(record["e"]) for record in employees]
        return nodes_json

# Find all employees:
def find_all_employees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (e:Employee)"
                                "RETURN e;")
        nodes_json = [node_to_json(record["e"]) for record in employees]
        return nodes_json

# # Updating customer information
def update_employee (employee_id, name, address, branch):
    with _get_connection().session() as session:
        employees = session.run ("MATCH (e:Employee {employee_id: $employee_id})"
                                 "SET e.name = $name, e.address = $address, e.branch = $branch"
                                 "RETURN e;",
                                 employee_id = employee_id, name = name, address = address, branch = branch)
        nodes_json = [node_to_json(record["e"]) for record in employees]
        return nodes_json

#Deleting an employee
def delete_employee (employee_id):
    with _get_connection().session() as session:
        session.run("MATCH (e:Employee {employee_id: $employee_id})"
                                "DELETE e;",
                                employee_id = employee_id)


class Employee:
    def __init__(self, employee_id, name, address, branch):
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.branch = branch
    
    def get_Branch (self):
        return self.branch
    
    def set_Branch (self, new_branch):
        self.branch = new_branch
    
    def to_json(self):
        return {"employee_id": self.employee_id,
                "name": self.name,
                "address": self.address,
                "branch": self.branch}