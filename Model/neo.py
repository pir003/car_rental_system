from neo4j import GraphDatabase

# Oppsett av databaseforbindelsen
URI = "neo4j+s//09b7066b.databases.neo4j.io:7687"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def __get_connection():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver