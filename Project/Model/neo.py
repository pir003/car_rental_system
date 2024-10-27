from neo4j import GraphDatabase, Driver

# Oppsett av databaseforbindelsen
URI = "neo4j+ssc://09b7066b.databases.neo4j.io"
AUTH = ("neo4j", "1RWjhvw4XiA1EaB-OSmdOzdKgzP6e3rKvG77avLwHgU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver
    
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

def findUserByUsername(username):
    data = _get_connection().execute_query("MATCH (a:User) where a.username = $username RETURN a;", username=username)
    if len(data[0]) > 0:
        user = User (username, data[0] [0] [0] ['email'])
        return user
    else:
        return User (username, "Not found in DB")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def get_Username(self):
        return self.username
    
    def set_Username(self, value):
        self.username = value
    
    def get_Email(self):
        return self.email
    
    def set_Email(self, value):
        self.email = value

    
