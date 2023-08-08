import os
import sqlite3
from Hospital_Management.modules.administration import administration
from Hospital_Management.modules.patient_details import patient_details
from Hospital_Management.modules.user_management import registration, signin
# from Hospital_Management.modules.patient_details import assign_patient_to_doctor

def create_tables(cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patient_detail (
                name TEXT PRIMARY KEY,
                sex TEXT,
                age INTEGER,
                address TEXT,
                contact TEXT,
                disease TEXT,
                assigned_doctor TEXT
            )
            ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctor_details (
            name TEXT PRIMARY KEY,
            specialisation TEXT,
            age INTEGER,
            address TEXT,
            contact TEXT,
            fees INTEGER,
            monthly_salary INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nurse_details (
            name TEXT PRIMARY KEY,
            age INTEGER,
            address TEXT,
            contact TEXT,
            monthly_salary INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS other_workers_details (
            name TEXT PRIMARY KEY,
            age INTEGER,
            address TEXT,
            contact TEXT,
            monthly_salary INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            username TEXT PRIMARY KEY,
            password TEXT DEFAULT '000'
        )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assigned_patients (
                patient_name TEXT,
                doctor_name TEXT,
                FOREIGN KEY (patient_name) REFERENCES patient_detail(name),
                FOREIGN KEY (doctor_name) REFERENCES doctor_details(name)
            )
            ''')


def main():
    if not os.path.exists('database'):
        os.makedirs('database')

    conn = sqlite3.connect('database/city_hospitals.db')
    cursor = conn.cursor()

    create_tables(cursor)

    while True:
        print("""
            1. Sign In
            2. Registration
        """)

        choice = int(input("Enter your choice: "))

        if choice == 2:
            registration(conn, cursor)

        elif choice == 1:
            username, password = signin(cursor)
            if username and password:
                while True:
                    print("""
                        1. Administration
                        2. Patient (Details)
                        3. Sign Out
                    """)

                    action = int(input("Enter your choice: "))

                    if action == 1:
                        administration(conn, cursor)

                    elif action == 2:
                        patient_details(conn, cursor)

                    elif action == 3:
                        break

    conn.close()

if __name__ == "__main__":
    main()

