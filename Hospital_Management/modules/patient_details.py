def patient_details(conn,cursor):
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
            name, sex, age, address, contact, disease, assigned_doctor = row
            print(
                f"Name: {name}, Sex: {sex}, Age: {age}, Address: {address}, Contact: {contact}, Disease: {disease}, Assigned Doctor: {assigned_doctor}")
    elif patient_choice == 2:
        name = input("Enter your name: ")
        sex = input("Enter the gender: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        contact = input("Contact Details: ")
        disease = input("Enter patient's disease Related to: ")
        # assigned_doctor = input("Enter assigned doctor's name: ")
        cursor.execute("SELECT name, specialisation FROM doctor_details WHERE specialisation = ?", (disease,))
        doctors = cursor.fetchall()
        if doctors:
            print("Available doctors for this disease:")
            for doctor in doctors:
                print(doctor[0])
            doctor_name = input("Select a doctor from above list to assign the patient: ")
            assigned_doctor = doctor_name
            assign_patient_to_doctor(conn, cursor, name, doctor_name)

        else:
            print("No available doctor for this disease.")

        cursor.execute("INSERT INTO patient_detail VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, sex, age, address, contact, disease, assigned_doctor))
        conn.commit()
        print("Patient details added successfully.")
    elif patient_choice == 3:
        name = input("Enter the Patient Name: ")
        cursor.execute("DELETE FROM patient_detail WHERE name = ?", (name,))
        conn.commit()
        print("Patient details deleted.")


def assign_patient_to_doctor(conn, cursor, patient_name, doctor_name):
    cursor.execute("INSERT INTO assigned_patients (patient_name, doctor_name) VALUES (?, ?)", (patient_name, doctor_name))
    conn.commit()
    print(f"Patient '{patient_name}' has been assigned to Dr. {doctor_name}.")
    cursor.execute("UPDATE patient_detail SET assigned_doctor = ? WHERE name = ?", (doctor_name, patient_name))
    conn.commit()