import psycopg2
import PIvariables
# extablish connection to database and set variables connection and cursur

p = PIvariables.password

try: 
    conn = psycopg2.connect("host=localhost dbname=music user=postgres password={}".format(p))
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

# transactions table
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 (transaction_id int, \
                                                           customer_name varchar, cashier_id int, \
                                                           year int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# albums sold table
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (album_id int, transaction_id int, \
                                                        album_name varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# employees table
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS employees (employee_id int, \
                                                        employee_name varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# transactions table

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS sales (transaction_id int, \
                                                    amount_spent int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


# Close connection to database

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
      
