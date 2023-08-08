import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('../database/city_hospitals.db')

# details = conn.execute("pragma table_info('doctor_details')")
# print(details)
# for i in details:
#     print(i)

print("********************Doctor Details*********************")
res = conn.execute("SELECT * FROM doctor_details")
for i in res:
    print(i)


# details = conn.execute("pragma table_info('patient_detail')")
# print(details)
# for i in details:
#     print(i)

print("********************Patients Details*********************")
res = conn.execute("SELECT * FROM patient_detail")
for i in res:
    print(i)
#
# details = conn.execute("pragma table_info('nurse_details')")
# print(details)
# for i in details:
#     print(i)


print("********************Nurse Details*********************")
res = conn.execute("SELECT * FROM nurse_details")
for i in res:
    print(i)
#
# details = conn.execute("pragma table_info('other_workers_details')")
# print(details)
# for i in details:
#     print(i)

print("********************Other Staff Details*********************")
res = conn.execute("SELECT * FROM other_workers_details")
for i in res:
    print(i)

#
# details = conn.execute("pragma table_info('user_data')")
# print(details)
# for i in details:
#     print(i)

print("********************User Details*********************")
res = conn.execute("SELECT * FROM user_data")
for i in res:
    print(i)

#
#
# details = conn.execute("pragma table_info('assigned_patients')")
# print(details)
# for i in details:
#     print(i)

print("********************Doctor Assigned Details*********************")
res = conn.execute("SELECT * FROM assigned_patients")
for i in res:
    print(i)