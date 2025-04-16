'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

tasks = []

cet_students = {"Kazuzu", "Abdulli", "Rahul", "Seeyuhh"}
jee_students = {"Kazuzu", "Salmon", "Frank", "Abdulli"}
neet_students = {"Rahul", "Salmon", "Grace", "IceSpice"}

print("CET Students:", cet_students)
print("JEE Students:", jee_students)
print("NEET Students:", neet_students)

all_students = cet_students | jee_students | neet_students
common_students = cet_students & jee_students & neet_students
only_cet = cet_students - (jee_students | neet_students)

print("All Students Enrolled (Union):", all_students)
print("Students in All Exams (Intersection):", common_students)
print("Students Only in CET:", only_cet)

jee_neet_common = jee_students & neet_students
cet_jee_not_neet = (cet_students & jee_students) - neet_students

print("Students in Both JEE and NEET:", jee_neet_common)
print("Students in Both CET and JEE but Not in NEET:", cet_jee_not_neet)

exam = input("\nEnter exam to manage (CET, JEE, NEET): ").upper()
name = input("Enter student name: ")

if exam == "CET":
    cet_students.add(name)
elif exam == "JEE":
    jee_students.add(name)
elif exam == "NEET":
    neet_students.add(name)
else:
    print("Invalid exam name!")

print("\nUpdated CET Students:", cet_students)
print("Updated JEE Students:", jee_students)
print("Updated NEET Students:", neet_students)

