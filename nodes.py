from neo4j.v1 import GraphDatabase, basic_auth, session

try:
    db_location = "bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786"
    username = "jim"
    password = "b.SoW4Z3LwK2vB.xaS2VWcnFj6NfvAI"
    driver = GraphDatabase.driver(db_location,
                                  auth=basic_auth(username, password))
except:
    raise IOError("Couldn't connect to database.")
"""with self.driver.session() as session:
    db_user = session.run("MATCH (u:User {user_id: {uid}}) RETURN u",
                          {'uid': user_id}).single()['u']"""


def clear_database():
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session1 = driver.session()
    session1.run("MATCH (n) DETACH DELETE n")

def add_nodes():
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session = driver.session()

    # Make the album nodes
    session.run('''
        CREATE CONSTRAINT ON (a:album) ASSERT a.albumName IS UNIQUE;
        ''')
    session.run('''
        CREATE CONSTRAINT ON (s:song) ASSERT s.songName IS UNIQUE;
        ''')
    session.run('''
        CREATE CONSTRAINT ON (a:artist) ASSERT a.artistName IS UNIQUE;
        ''')

    session.run('''
        CREATE CONSTRAINT ON (f:feature) ASSERT f.artistName IS UNIQUE;
        ''')

    session.run('''
        USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS from 'https://s3-us-west-1.amazonaws.com/tim-test000/genius_short.csv' as line
        MERGE (album:Album {albumName: line.Album, albumYear: line.Year})
        MERGE (artist:Artist {artistName: line.Artist})
        MERGE (song:Song {songName: line.Song})
        MERGE (artist)-[:CREATED]->(album)
        CREATE (album)-[:HAS_SONG]->(song)
        WITH line
        WHERE NOT line.Feature1 IS NULL
        MERGE (feature:Artist {artistName: line.Feature1})
        MERGE (song:Song {songName: line.Song})-[:FEATURES]->(feature)
        ''')

clear_database()
add_nodes()