from calendar import calendar
from winsound import MB_ICONASTERISK
import numpy as np
import math

# 2 . input student information
class Student:
    count=0 # thuộc tính có sẵn đếm số lần tạo mới của class
    pass
    #initializer / object attributes
    def __init__(self,id,name,dob):
        print("Enter the student information : ")
        self.id=id  
        self.name=name
        self.dob=dob
        Student.count +=1
        
    #id
    def get_id(self):
        return self.id
    #name
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    #dob
    def set_dob(self,dob):
        self.dob = dob
    def get_dob(self):
        return self.dob

    def StudentInformation(self):
        print(f"ID : {self.get_id()}")
        print(f"Student name : {self.name}")
        print(f"Student dob : {self.dob}")


#4. input courses information :
class Course :
    count = 0
    pass
    def __init__(self,courseID,courseName,mark):
        self. courseID=courseID 
        self.courseName=courseName
        self.mark=mark
        Course.count +=1
        B = {"id":courseID,"name":courseName,"mark":mark}
        Course.append(B)
    #courseID
    def set_courseID(self,courseID):
        self.courseID = courseID
    def get_courseID(self):
        return self.courseID
    #courseName
    def set_courseName(self,courseName):
        self.courseName = courseName
    def get_courseName(self):
        return self.courseName
    #mark
    def set_mark(self,mark):
        self.mark = mark
    def get_mark(self):
        return self.mark

    def CourseInformation(self):
        print(f"ID : {self.courseID()}")
        print(f"Student name : {self.courseName}")
        print(f"Student dob : {self.mark}")

#1. input number of students in a class
def CountStudents():
	count = int(input("How many students are there in the class ?"))
	return count

#3. input number of courses :
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses

list_system = []
while True :
    print(f'''\n
    0.close tab
    1.number of student
    2.delete student from course
    3.number of course
    4.delete course
    ''')
    select = input("Enter your choice : ")

    if str(select).isdigit():
        select = int(select)
        if select == 0 :
            break
        elif select == 1:
            CountStudents = int(input("Enter the number of student in the course :"))
            for i in range(CountStudents):
                f = open("data.txt","a")
                id = input("Enter the student ID:")
                name = input("Enter the student name :")
                dob = input("Enter the student dob :")
                A = {"id":id , "name": name , "dob": dob}
                st = Student(id,name,dob)
                list_system.append(st)
                f.write(f"{id},{name},{dob}\n")
                f.close()
                
            for i in range(list_system.__len__()):
                print(list_system[i])
            def StudentList(Students):
                for A in Students :
                    print(f"id {A['id']},name is {A['name']},DOB is {A['DOB']} ")

        elif select == 2 :
            id = input("Enter the student ID must change : ")
            for i in list_system:
                if i.get_id() == id:
                    i.set_name(input("Enter the new student name : "))
                    i.set_dob(input("Enter the new student dob : "))
                    i.StudentInformation()

        elif select == 3 :
            tpmMark = []
            NumberOfCourse = int(input("Enter number of course : "))            
            for i in range(NumberOfCourse):
                g = open ("data.txt","a")
                courseID = input("Enter the Course ID : ")
                courseName = input("Enter the course name : ")
                mark = float(input("Enter the mark : "))
                course = Course(courseID,courseName,mark)
                B = {"courseID":courseID,"courseName":courseName,"mark":mark}
                tpmMark.append(mark)
                list_system.append(course)
                g.write(f"{courseID},{courseName},{mark}/n")
                g.close()
            for i in range(list_system.__len__()):
                print(list_system[i])
            print("Do you want to calculate the student's GPA ? ")
            print("Oui or Non")
            choose = str(input("Enter your choose : "))
            if choose == "Oui":
                print(np.average(tpmMark))
            else :
                break
            def CoursesList(Courses):
	            for B in Courses:
		             print(f"courseID {B['courseID']},courseName is {B['courseName']},mark is {B['mark']}")

        
        elif select == 4 :
            courseID = input("Enter the course ID must change : ")
            for i in list_system:
                if i.set_courseID() == courseID:
                    i.set_courseName("Enter the new course name : ")
                    i.set_mark("Enter the new course mark")
                    i.CourseInformation()
    else:
        print("You must enter a number . Please enter again !")

print("All Students:")
StudentList(Student)
print("All Courses:")
CoursesList(Course)