LOAD CSV WITH HEADERS FROM "file:///CourseWork.csv" AS line
CREATE (bulk :Bulk)-[:SENT]->(country :Country)
SET bulk.name = line.Bulk