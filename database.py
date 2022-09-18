
import psycopg2

class DatabaseConnection:

    def __init__(self):
        #grab connection config parameters
        connection_str = open('resources\pgpass').read().replace('\n','')
        configs = connection_str.split(':')
        self.host = configs[0]
        self.port = configs[1]
        self.database = configs[2]
        self.user = configs[3]
        self.password = configs[4]

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(
                host=self.host, 
                database=self.database, 
                user=self.user, 
                password=self.password, 
                port=self.port)
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error connecting to DB: {}'.format(error))
            raise error
        return conn