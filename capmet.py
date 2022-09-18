import sys
# use ijson library to avoid reading entire file into memory at once
import ijson
from database import DatabaseConnection
from psycopg2 import DatabaseError
from tripdata import TripData

# read in JSON data and insert into DB
conn = None
try:    
    if sys.argv.__len__() < 2:
        raise Exception('Usage: Pass in filename argument')
    file_name = sys.argv[1]
    conn = DatabaseConnection().connect()
    [TripData(item).insert(conn) for item in ijson.items(open(file_name),'item')]
    conn.commit()
except (Exception, DatabaseError) as error:
     print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
