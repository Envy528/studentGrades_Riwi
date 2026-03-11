studentsList = []
option = None

while option != 2:
    option = input("\n1. Register a student.\n2. Show registered students.\n3. Leave.\nChoose an option: ")

    if option == "1":
        try:
            studentsQuantity = int(input("\nHow many students are you going to register?\nNumber: "))
        
            for i in range(studentsQuantity):
                subjectsAndGrades = []
                studentFullName = input(f"\nEnter the {i+1} student's full name.\nFull name: ")
                
                subjectQuantity = int(input("\nHow many subjects are you going to register for this student?\nNumber: "))
                
                for i in range(subjectQuantity):
                    subject = input(f"\nEnter the {i+1} subject for the student.\nSubject: ")
                    grade = float(input(f"\nEnter the {subject} grade.\nGrade: "))

                    subjectsAndGrades.append({
                        "subject":subject,
                        "grade":grade,
                    })
                
                
                studentsList.append({
                    "studentName":studentFullName,
                    "subjectsAndGrades":subjectsAndGrades
                })

        except:
            print("\n----- ERROR -----\nEnter a valid number")


    elif option == "2":
        print("\n----- Students -----")
        for i, student in enumerate(studentsList):
            print(f"{i+1}. {student['studentName']}\n")
            
            for i, studentSubjectAndGrade in enumerate(student["subjectsAndGrades"]):
                print(f"{i+1}--Subject: {studentSubjectAndGrade['subject']}\n----Grade: {studentSubjectAndGrade['grade']}\n")
        print("-"*20)
    else:
        print("Choose a valid option.")
