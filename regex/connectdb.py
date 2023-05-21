import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="airlines",
    user="postgres",
    password="ruhulamin"
)

# Create a cursor object
cursor = conn.cursor()

try:
    # Execute a query to retrieve the data
    #cursor.execute("SELECT * FROM pax_master where flight_date")
    cursor.execute("""
    SELECT flight_code, flight_date, COUNT(*) as count
        FROM pax_master
        GROUP BY flight_code, flight_date
        HAVING COUNT(*) > 1
    """)
    # Fetch all the rows
    rows = cursor.fetchall()

    # Process and print the retrieved data
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error retrieving data from PostgreSQL:", error)

finally:
    # Close the cursor and the connection
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
