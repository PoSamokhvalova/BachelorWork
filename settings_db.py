import data_helpers

driver = data_helpers.driver

link_data = 'https://raw.githubusercontent.com/PoSamokhvalova/BachelorWork/master/CourseWork.csv'


def clear_db():
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")


def set_constraint():

    with driver.session() as session:
        session.run("CREATE CONSTRAINT ON (bulk :Bulk) ASSERT bulk.name is UNIQUE")


def uload_data():

    with driver.session() as session:
        session.run("LOAD CSV WITH HEADERS FROM '{}' AS line ".format(link_data) +
                    "MERGE (bulk :Bulk {name: line.Bulk}) " +
                    "MERGE (aggregator :Aggregator {name: line.Aggregator}) "
                    "MERGE (operator :Operator {name: line.Operator}) "
                    "MERGE (bulk)-[:SENT{price: line.Price_b}]->(aggregator)-[:SENT{price: line.Price_a}]->(operator) "
        )

clear_db()
set_constraint()
uload_data()