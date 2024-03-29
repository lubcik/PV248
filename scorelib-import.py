import re # regular expressions
import sqlite3

# This is a base class for objects that represent database items. It implements
# the store() method in terms of fetch_id and do_store, which need to be
# implemented in every derived class (see Person below for an example).

class DBItem:
    def __init__( self, conn ):
        self.id = None
        self.cursor = conn.cursor()

    def store( self ):
        self.fetch_id()
        if ( self.id is None ):
            self.do_store()
            self.cursor.execute( "select last_insert_rowid()" )
            self.id = self.cursor.fetchone()[ 0 ]

# Example of a class which represents a single row of a single database table.
# This is a very simple example, since it does not contain any references to
# other objects.


class Person( DBItem ):
    def __init__( self, conn, string ):
        super().__init__( conn )
        self.born = self.died = None
        self.name = re.sub( '\([0-9/+-]+\)', '', string ).strip()

        m = re.search( "([0-9]+)--([0-9]+)", string )
        if not m is None:
            self.born = int( m.group( 1 ) )
            self.died = int( m.group( 2 ) )


    def fetch_id( self ):
        self.cursor.execute( "select id from person where name = ?", (self.name,) )

        res = self.cursor.fetchone()
        if not res is None: # TODO born/died update should be done inside this if
            self.id = res[ 0 ]
            self.cursor.execute(
                "update person set born = ?, died = ? where id = ?", (
                    self.born, self.died, self.id))


    def do_store( self ):
        print ("storing '%s'" % self.name)
        # NB. Part of the exercise was adding the born/died columns to the below query.
        self.cursor.execute( "insert into person (name, born, died) values (?, ?, ?)",
                             ( self.name, self.born, self.died ) )


# Process a single line of input.
def process( k, v ):
    if k == 'Composer' or k == 'Editor':
        for c in v.split(';'):
            p = Person( conn, c.strip() )
            p.store()


# Database initialisation: sqlite3 scorelib.dat ".read scorelib.sql"
conn = sqlite3.connect( 'scorelib.dat' )
rx = re.compile( r"(.*): (.*)" )
for line in open( 'scorelib.txt', 'r', encoding='utf-8' ):
    m = rx.match( line )
    if m is None: continue
    process( m.group( 1 ), m.group( 2 ) )

conn.commit()