import data_helpers

driver = data_helpers.driver


def clear_db():
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")


def set_constraint():

    with driver.session() as session:
        session.run("CREATE CONSTRAINT ON (bulk :Bulk) ASSERT bulk.name is UNIQUE")


clear_db()
set_constraint()
