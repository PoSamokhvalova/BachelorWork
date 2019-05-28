from neo4j import GraphDatabase, basic_auth

# connection

db_location = "bolt://35.204.38.2"
username = "neo4j"
password = "unegon23"
driver = GraphDatabase.driver(db_location,auth = basic_auth(username, password))

# ------- algo ------


def calculate_neo4j_price(country):

    with driver.session() as session:

        result = session.run("MATCH (bulk :Bulk)-[v1 :SENT]->(aggregator :Aggregator)-[v2 :SENT]->(operator :Operator)-[:IN_THE]->(country :Country) "
                             "WHERE country.name = $COUNTRY "
                             "WITH min(v1.price+v2.price) AS price_min "
                             "RETURN price_min AS price"
                             , {'COUNTRY': country})

        return result.single()['price']
