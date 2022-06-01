import psycopg2


# extablish connection to database and set variables connection and cursur

try: 
    conn = psycopg2.connect("host=localhost dbname=music user=postgres password=*****")
    print('connected to new database')
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)

try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

try:
    cur.close()
    print('closed curser')
except psycopg2.Error as e:
    print("Error: could not close curser")
    print(e)

try:
    conn.close()
    print('closed connection')
except psycopg2.Error as e:
    print('Error: could not close connection')
    print(e)