from passwords import PASSWORD
from flask import Flask
from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__)
password = 'neo4j'
username = 'neo4j'
db_location = 'localhost:11001'
driver = GraphDatabase.driver(db_location, auth=basic_auth(username, password))

def directed(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:Person)-[:directed]->(f) "
                                 "WHERE a.name = {name} "
                                 "RETURN f.name", name=name):
                print(record["f.name"])

directed("Andy Wachowski")

