if select == 0 :
            break
        elif select == 1:
            CountStudents = int(input("Enter the number of student : "))
            for i in range(CountStudents):
                id = input("Enter the student ID:")
                name = input("Enter the student name :")
                dob = input("Enter the student dob :")
                st = Student(id,name,dob)
                list_system.append(st)
            for i in range(list_system.__len__()):
                print(list_system[i])

        elif select == 3 :
            id = input("Enter the student ID must change : ")
            for i in list_system:
                if i.get_id() == id:
                    i.set_name(input("Enter the new student name : "))
                    i.set_dob(input("Enter the new student dob : "))
                    i.StudentInformation()

        elif select == 4 :
            tpmMark = []
            NumberOfCourse = int(input("Enter number of course : "))            
            for i in range(NumberOfCourse):
                courseID = input("Enter the Course ID : ")
                courseName = input("Enter the course name : ")
                mark = float(input("Enter the mark : "))
                course = Course(courseID,courseName,mark)
                tpmMark.append(mark)
                list_system.append(course)
            for i in range(list_system.__len__()):
                print(list_system[i])
            print("Do you want to calculate the student's GPA ? ")
            print("Oui or Non")
            choose = str(input("Enter your choose : "))
            if choose == "Oui":
                print(np.average(tpmMark))
            else :
                break

        elif select == 6 :
            courseID = input("Enter the course ID must change : ")
            for i in list_system:
                if i.set_courseID() == courseID:
                    i.set_courseName("Enter the new course name : ")
                    i.set_mark("Enter the new course mark")
                    i.CourseInformation()

    else:
        print("You must enter a number . Please enter again !")