studentsList = []
option = None

while option != 2:
    option = input("\n1. Register a student\n2. Show registered students\n3. Leave\nChoose an option: ")

    if option == "1":
        try:
            studentsQuantity = int(input("\nHow many students are you going to register?\nNumber: "))
        
            for i in range(studentsQuantity):
                studentFullName = input(f"\nEnter the {i+1} student's full name\nFull name: ")
                
                studentsList.append(studentFullName)

        except:
            print("\n----- ERROR -----\nEnter a valid number")


    elif option == "2":
        print("\n----- Students -----")
        for i, student in enumerate(studentsList):
            print(f"{i+1}. {student}")
        print("-"*20)
    
    else:
        print("Choose a valid option.")
