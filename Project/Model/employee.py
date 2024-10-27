from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

# Creating an employee
def createEmployee (employee_id, name, address, branch):
    _get_connection().execute_query(""" CREATE (e:Employee {employee_id: $employee_id, name: $name, address: $address, branch = $branch})""", employee_id = employee_id, name = name, address = address, branch = branch)

# Reading an employee
def findEmployeeById(employee_id):
    data = _get_connection().execute_query("MATCH (e:Employee) where e.employee_id = $employee_is RETURN e", employee_id=employee_id)
    if len(data[0]) > 0:
        employee = Employee (employee_id, data[0] [0] [0]['name', 'address', 'branch'])
        return employee
    else:
        return Employee (employee_id, "Not found in DB")

# # Updating customer information
def updateEmployee (employee_id, name=None, address=None, branch=None):
    updates = []
    if name is not None:
        updates.append("e.name = $name")
    if address is not None:
        updates.append("e.address =$address")
    if branch is not None:
        updates.append("e.branch = $branch")
    database_update = ", ".join(updates)
    query = f"MATCH (e.Employee) where e.employee_id = $employee_id SET {database_update}"
    _get_connection().execute_query(query, employee_id = employee_id, name = name, address = address, branch = branch)

#Deleting an employee
def deleteEmployee (employee_id):
    _get_connection().execute_query("MATCH (e.Employee) where e.employee_id = $employee_id DELETE e", employee_id = employee_id)

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