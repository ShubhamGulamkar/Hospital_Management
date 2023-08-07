import sqlite3

def registration(conn, cursor):
    print("===========================================")
    print("!!!!!!!!! Register Yourself !!!!!!!!")
    print("===========================================")
    username = input("Input your username: ")
    password = input("Input the password (Password must be strong!): ")

    try:
        cursor.execute("INSERT INTO user_data VALUES (?, ?)", (username, password))
        conn.commit()
        print("===========================================")
        print("!! Well Done!! Registration Done Successfully!!")
        print("===========================================")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")

    input("Enter any key to continue: ")


def signin(cursor):
    print("===========================================")
    print("!!!!!!! {{Sign In}} !!!!!!!!!")
    print("===========================================")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    cursor.execute("SELECT password FROM user_data WHERE username = ?", (username,))
    row = cursor.fetchone()

    if row and row[0] == password:
        print("Sign-in successful.")
        return username, password
    else:
        print("Username or password is incorrect.")
        return None, None
