import sqlite3

# conn = sqlite3.connect('gtav_cars.db')

# cursor = conn.cursor()
# cursor.execute("""
#             CREATE TABLE cars
#             (id int, name varchar(255), photo varchar(255))
#             """)
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(carId, name, photo):
    # try:
    with sqlite3.connect('gtav_cars.db') as sqliteConnection:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO cars
                                    (id, name, photo) VALUES (?, ?, ?)"""
        carImg = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (carId, name, carImg)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        # cursor.close()
        # except sqlite3.Error as error:
        #     print("Failed to insert blob data into sqlite table", error)
        # finally:
        # if sqliteConnection:
        #     sqliteConnection.close()
        print("the sqlite connection is closed")

# insertBLOB('1', 'Turismo R', './Turismo_R.png' )


