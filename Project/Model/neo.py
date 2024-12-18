from neo4j import GraphDatabase, Driver

# Creating a database connection:
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver


# Method for testing the connection:    
def test_connection():
    driver = None
    try:
        driver = GraphDatabase.driver(URI, auth=AUTH)
        driver.verify_connectivity()
        print("Tilkobling til Neo4j er vellykket!")
    except Exception as e:
        print(f"Tilkobling til Neo4j feilet: {e}")
    finally:
        driver.close()


if __name__ == "__main__":
    test_connection()



    
