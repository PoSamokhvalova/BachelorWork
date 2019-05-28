from neo4j import GraphDatabase, basic_auth

# connection

db_location = "bolt://35.204.38.2"
username = "neo4j"
password = "unegon23"
driver = GraphDatabase.driver(db_location,auth = basic_auth(username, password))

# ------- algo ------

def calculate_neo4j_price():

    with driver.session() as session:

        result = session.run("RETURN rand() AS price")

        return result.single()['price']
