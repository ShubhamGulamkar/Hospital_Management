def patient_details(cursor):
    print("""
        1. Show Patients Info
        2. Add New Patient
        3. Discharge Summary
        4. Exit
    """)

    patient_choice = int(input("Enter your choice: "))

    if patient_choice == 1:
        cursor.execute("SELECT * FROM patient_detail")
        rows = cursor.fetchall()
        for row in rows:
            name, sex, age, address, contact = row
            print(f"Name: {name}, Sex: {sex}, Age: {age}, Address: {address}, Contact: {contact}")
    elif patient_choice == 2:
        name = input("Enter your name: ")
        sex = input("Enter the gender: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        contact = input("Contact Details: ")
        cursor.execute("INSERT INTO patient_detail VALUES (?, ?, ?, ?, ?)",
                       (name, sex, age, address, contact))
        print("Patient details added successfully.")
    elif patient_choice == 3:
        name = input("Enter the Patient Name: ")
        cursor.execute("DELETE FROM patient_detail WHERE name = ?", (name,))
        print("Patient details deleted.")
