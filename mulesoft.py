import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='movies',
                                         user='root',
                                         password='sarvin@123')

    sql_select_Query = "select * from movies"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("moviename = ", row[1])
        print("actorname  = ", row[2])
        print("release date  = ", row[3])
        print("director name  = ", row[4],"\n")



except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")