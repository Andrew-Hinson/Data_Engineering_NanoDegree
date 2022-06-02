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

# 3 way join to illustrate point

try: 
    cur.execute("SELECT transactions2.transaction_id, \
                transactions2.customer_name, \
                employees.employee_name, \
                transactions2.year, \
                albums_sold.album_name, \
                sales.amount_spent \
                FROM transactions2 \
                JOIN employees \
                ON transactions2.cashier_id = employees.employee_id \
                JOIN albums_sold \
                ON transactions2.transaction_id = albums_sold.transaction_id \
                JOIN sales \
                ON transactions2.transaction_id = sales.transaction_id")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

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