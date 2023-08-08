def administration(conn,cursor):
    print("""
        1. Display the details
        2. Add a new member
        3. Delete a member
        4. Make an exit
    """)

    admin_choice = int(input("Enter your choice: "))

    if admin_choice == 1:
        print("""
            1. Doctors Details
            2. Nurse Details
            3. Others
        """)

        details_choice = int(input("Enter your Choice: "))
        if details_choice == 1:
            print("THE DOCTORS AVAILABLE ARE:\n")
            cursor.execute("SELECT * FROM doctor_details")
            rows = cursor.fetchall()
            for row in rows:
                name, specialisation, age, address, contact, fees, monthly_salary = row
                print(f"Name: {name}, Specialisation: {specialisation}, Age: {age}, Address: {address}, Contact: {contact}, Fees: {fees}, Monthly Salary: {monthly_salary}")
        elif details_choice == 2:
            print("THE NURSES AVAILABLE ARE:\n")
            cursor.execute("SELECT * FROM nurse_details")
            rows = cursor.fetchall()
            for row in rows:
                name, age, address, contact, monthly_salary = row
                print(f"Name: {name}, Age: {age}, Address: {address}, Contact: {contact}, Monthly Salary: {monthly_salary}")
        elif details_choice == 3:
            print("THE STAFF AVAILABLE ARE:\n")
            cursor.execute("SELECT * FROM other_workers_details")
            rows = cursor.fetchall()
            for row in rows:
                name, age, address, contact, monthly_salary = row
                print(f"Name: {name}, Age: {age}, Address: {address}, Contact: {contact}, Monthly Salary: {monthly_salary}")

    elif admin_choice == 2:
        print("""
            1. Doctor Details
            2. Nurse Details
            3. Others
        """)

        add_choice = int(input("Enter your Choice: "))
        if add_choice == 1:
            name = input("Enter the doctor's name: ")
            specialisation = input("Enter the specialization of Doctor: ")
            age = int(input("Enter the age: "))
            address = input("Enter the address: ")
            contact = input("Enter Contact Details: ")
            fees = int(input("Enter the fees: "))
            monthly_salary = int(input("Enter Monthly Salary: "))
            cursor.execute("INSERT INTO doctor_details VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (name, specialisation, age, address, contact, fees, monthly_salary))
            conn.commit()
            print("Successfully added doctor details.")
        elif add_choice == 2:
            name = input("Enter Nurse name: ")
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            contact = input("Enter Contact No: ")
            monthly_salary = int(input("Enter Monthly Salary: "))
            cursor.execute("INSERT INTO nurse_details VALUES (?, ?, ?, ?, ?)",
                           (name, age, address, contact, monthly_salary))
            conn.commit()
            print("Successfully added nurse details.")
        elif add_choice == 3:
            name = input("Enter worker name: ")
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            contact = input("Enter Contact No.: ")
            monthly_salary = int(input("Enter Monthly Salary: "))
            cursor.execute("INSERT INTO other_workers_details VALUES (?, ?, ?, ?, ?)",
                           (name, age, address, contact, monthly_salary))
            conn.commit()
            print("Successfully added worker details.")

    elif admin_choice == 3:
        print("""
            1. Doctor Details
            2. Nurse Details
            3. Others
        """)

        delete_choice = int(input("Enter your Choice: "))
        if delete_choice == 1:
            name = input("Enter Doctor's Name: ")
            cursor.execute("DELETE FROM doctor_details WHERE name = ?", (name,))
            print("Doctor details deleted.")
        elif delete_choice == 2:
            name = input("Enter Nurse Name: ")
            cursor.execute("DELETE FROM nurse_details WHERE name = ?", (name,))
            print("Nurse details deleted.")
        elif delete_choice == 3:
            name = input("Enter the worker Name: ")
            cursor.execute("DELETE FROM other_workers_details WHERE name = ?", (name,))
            print("Worker details deleted.")
