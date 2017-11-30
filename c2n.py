from neo4j.v1 import GraphDatabase, basic_auth, session

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
        LOAD CSV WITH HEADERS from 'https://s3-us-west-1.amazonaws.com/tim-test000/example.csv' as line

        MERGE (album:Album {albumName: line.Album, albumYear: line.Year})
        MERGE (artist:Artist {artistName: line.Artist})
        MERGE (song:Song {songName: line.Song})
        MERGE (feature:Artist {artistName: line.Feature1})

        MERGE (artist)-[:CREATED]->(album)
        CREATE (album)-[:HAS_SONG]->(song)
        CREATE (song)-[:FEATURES]->(feature)
        ''')

def add_nodes_1():
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
add_nodes_1()


"""
def add_songs():
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session = driver.session()
    # Make the songs nodes
    session.run('''
            CREATE CONSTRAINT ON (s:song) ASSERT s.songName IS UNIQUE;
            ''')
    session.run('''
            CREATE CONSTRAINT ON (f:feature) ASSERT f.artistName IS UNIQUE;
    ''')

    session.run('''
            USING PERIODIC COMMIT
            LOAD CSV WITH HEADERS from 'https://s3-us-west-1.amazonaws.com/tim-test000/example.csv' as line
            MERGE (feature:Feature {artistName: line.Feature})
            CREATE (song:Song {songName: line.Song})
            CREATE (song)-[:FEATURING]->(feature)
        ''')


def add_artists():
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session = driver.session()

    # Make the artist nodes
    session.run('''
            CREATE CONSTRAINT ON (a:artist) ASSERT a.artistName IS UNIQUE;
            ''')

    session.run('''
            USING PERIODIC COMMIT
            LOAD CSV WITH HEADERS from 'https://s3-us-west-1.amazonaws.com/tim-test000/example.csv' as line
            MERGE (artist:Artist {artistName: line.Artist})
        ''')

#add_artists()
#add_songs()

#MERGE (feature:Feature {featuredArtist: line.Feature})


def add_features(self):
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session = driver.session()
    # session.run("MATCH (n) DETACH DELETE n")

    # Make the featured artist node
    session.run('''
               LOAD CSV WITH HEADERS FROM 'https://s3-us-west-1.amazonaws.com/tim-test000/example.csv' AS row
               CREATE (:Featured {year: row.Feature})
               ''')
"""
"""
def add_years():
    driver = GraphDatabase.driver("bolt://hobby-adojaekaoeaggbkeneahlppl.dbs.graphenedb.com:24786",
                                  auth=basic_auth("tim", "b.kHewn8yXyIvl.NGu5wpOxTNgCoSmq"))
    assert isinstance(driver, object)
    session = driver.session()
    # Make the year nodes
    session.run('''
                CREATE CONSTRAINT ON (y:year) ASSERT y.Year IS UNIQUE;
                ''')

    session.run('''
                USING PERIODIC COMMIT
                LOAD CSV WITH HEADERS from 'https://s3-us-west-1.amazonaws.com/tim-test000/example.csv' as line
                MERGE (year:Year {year: line.Year})
            ''')
"""




"""
    def main(self):
        add_artists_albums_songs()
        add_years_features()

add_artists()
add_albums()
"""


#add_years()

#MERGE (song:Song {songName: line.Song})
#//copy all properties
#MATCH (n:Artist), (m:Feature) WHERE n.artistName = m.ArtistName WITH n, m SET n += m;


#MERGE (feature:Feature {artistName: line.Feature})
# MERGE (artist:Artist {artistName: line.Feature})
'''
        //copy all outgoing relations
        MATCH (n:Artist), (m:Feature)-[r:FEATURES]->(endnode) WHERE n.artistName = m.artistName
        WITH n, collect(endnode) as endnodes
        FOREACH (x in endnodes | CREATE (n)-[:CREATED]->(x));

        //copy all incoming relations
        MATCH (n:Artist), (m:Features)<-[r:FEATURES]-(endnode) WHERE n.artistName = m.artistName
        WITH n, collect(endnode) as endnodes
        FOREACH (x in endnodes | CREATE (n)<-[:FEATURES]-(x));

        //delete duplicates
        MATCH (n:Artist), (m:Features) WHERE n.artistName = m.artistName detach delete m;'''
