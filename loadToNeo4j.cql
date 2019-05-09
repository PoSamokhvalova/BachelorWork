LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/PoSamokhvalova/BachelorWork/master/CourseWork.csv?token=AL4C7VAV2BXUDO76PUOCRIS42P5BY" AS line
CREATE (bulk :Bulk)-[:SENT]->(country :Country)
SET bulk.name = line.Bulk, bulk.price = line.Price, country.name = line.Country