import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('city_hospitals.db')

# details = conn.execute("pragma table_info('doctor_details')")
# print(details)
# for i in details:
print("\n\n")

print("********************Doctor Details*********************\n")


res = conn.execute("SELECT * FROM doctor_details")
for i in res:
    print(i)


# details = conn.execute("pragma table_info('patient_detail')")
# print(details)
# for i in details:
#     print(i)
print("\n")
print("********************Patients Details*********************\n")


res = conn.execute("SELECT * FROM patient_detail")
for i in res:
    print(i)
#
# details = conn.execute("pragma table_info('nurse_details')")
# print(details)
# for i in details:
#     print(i)

print("\n")
print("********************Nurse Details*********************\n")


res = conn.execute("SELECT * FROM nurse_details")
for i in res:
    print(i)
#
# details = conn.execute("pragma table_info('other_workers_details')")
# print(details)
# for i in details:
#     print(i)
print("\n")
print("********************Other Staff Details*********************\n")


res = conn.execute("SELECT * FROM other_workers_details")
for i in res:
    print(i)

#
# details = conn.execute("pragma table_info('user_data')")
# print(details)
# for i in details:
#     print(i)
print("\n")
print("********************User Details*********************\n")


res = conn.execute("SELECT * FROM user_data")
for i in res:
    print(i)

#
#
# details = conn.execute("pragma table_info('assigned_patients')")
# print(details)
# for i in details:
#     print(i)
print("\n")
print("********************Doctor Assigned Details*********************\n")


res = conn.execute("SELECT * FROM assigned_patients")
for i in res:
    print(i)