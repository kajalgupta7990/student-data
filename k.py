import matplotlib.pyplot as plt
import pandas as pd

student = []
def addStudent():
    n = 4
    sid = input("enter the id:")
    sname = input("enter the name:")
    age = int(input("enter the age"))
    course = input("enter the course type:")
    marks = []

    subjects = []

    for i in range(n):
        sub = input("Enter subject name: ")
        m = int(input("Enter marks: "))

        subjects.append(sub)
        marks.append(m)

    students = {
    "id": sid,
    "name": sname,
    "age": age,
    "course": course,
    "subject": subjects,
    "marks": marks
    }

    student.append(students)
    print(student)

def search():
    sid = input("Enter ID to search: ")
    found = False

    for i in student:   
        if i["id"] == sid:
            print("\n--- Student Found ---")
            print("ID:", i["id"])
            print("Name:", i["name"])
            print("Age:", i["age"])
            print("Course:", i["course"])

            print("Subjects and Marks:")
            for s, m in zip(i["subject"], i["marks"]):
                print(s, ":", m)

            found = True
            break

            if not found:
                print("\nStudent not found")

def update():
    sid = input("Enter ID to update: ")
    found = False

    for i in student:
        if i["id"] == sid:

            print("1. Name")
            print("2. Course")
            print("3. Marks")

            ch = input("What you want to update: ")

            if ch == "1":
                newname = input("Enter new name: ")
                i["name"] = newname

            elif ch == "2":
                newcourse = input("Enter new course: ")
                i["course"] = newcourse

            elif ch == "3":
                print("Subjects:", i["subject"])
                pos = int(input("Which subject number to update: ")) - 1
                newmarks = int(input("Enter new marks: "))
                i["marks"][pos] = newmarks

            print("Updated successfully")
            found = True
            break

    if not found:
        print("Student not found")

def delete():
    sid = input("Enter ID to delete: ")
    found = False

    for i in student:
        if i["id"] == sid:
            student.remove(i)
            print("Student deleted successfully")
            found = True
            break

    if not found:
        print("Student not found")
def showALL():
    df = pd.DataFrame(student)
    print(df)

def showGraph():
    sid = input("Enter ID to show graph: ")
    found = False

    for i in student:
        if i["id"] == sid:
            subjects = i["subject"]
            marks = i["marks"]

            plt.bar(subjects, marks)
            plt.xlabel("Subjects")
            plt.ylabel("Marks")
            plt.title("Marks of " + i["name"])
            plt.show()

            found = True
            break

    if not found:
        print("Student not found")







while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students (Pandas)")
    print("6. Show Marks Graph (Matplotlib)")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        addStudent()
    elif ch == "2":
        search()
    elif ch == "3":
        update()
    elif ch == "4":
        delete()
    elif ch == "5":
        showALL()
    elif ch == "6":
        showGraph()
    elif ch == "7":
        print("Thank you baby ❤️ Program ended.")
        break
    else:
        print("Invalid choice, try again")
