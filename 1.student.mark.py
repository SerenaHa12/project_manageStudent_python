

#1. input number of students in a class
from calendar import c
from winsound import MB_ICONASTERISK
def CountStudents():
	count = int(input("How many students are there in the class ?"))
	return count


#2. input student information 
def Studentinformation():
	print("Enter your Student Information : ")
	id = input(" Enter the student ID : ")
	name = input(" Enter the student Name : ")
	DOB = input(" Enter the student DOB : ")
	A = {"id":id,"name":name,"DOB":DOB}
	return A

def StudentsList(Students):
	for A in Students:
		print(f"id {A['id']},name is {A['name']},DOB is {A['DOB']} ")


#3. input number of courses
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses


#4. input courses information :
def CourseInformation() :
    print("Enter the Course Information :")
    id = input("Enter the course id : ")
    name = input("Enter the course name : ")
    mark = input("Enter the mark of course :")
    B = {"id":id,"name":name,"mark":mark}
    return B

def CoursesList(Courses):
	for B in Courses:
		print(f"id {B['id']},name is {B['name']},mark is {B['mark']}")


#5. select a course , input marks for student in this coures 

# main 
Students = []
count = CountStudents()
for i in range(0,count):
	C = Studentinformation()
	Students += [ C ] 


# main 
Courses = []
count = NumberOfCourses()
for i in range(0,count):
	D =  CourseInformation()
	Courses += [ D ]

#hi

print("All Students:")
StudentsList(Students)
print("All Courses:")
CoursesList(Courses)