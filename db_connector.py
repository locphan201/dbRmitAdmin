import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )
    cursor = mydb.cursor()
    db = "USE nanasbakery;"
    cursor.execute(db)
    return mydb, cursor

def disconnect_db(mydb, cursor):
    cursor.close()
    mydb.close()
    return mydb, cursor

def check_login(account, password):
    mydb, cursor = connect_db()
    query = """SELECT pwd FROM administration WHERE account='%s'""" %account
    cursor.execute(query)
    result = cursor.fetchall()
    mydb, cursor = disconnect_db(mydb, cursor)
    if len(result) == 0:
        return False
    else:
        return result[0][0] == password