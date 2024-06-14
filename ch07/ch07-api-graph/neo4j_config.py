from py2neo import Graph

def db_auth():
    graph = Graph("bolt://127.0.0.1:7687", auth=("neo4j", "packt2255"))
    return graph