#1. input number of students in a class
def CountStudents():
	CountStudents = int(input("How many students are there in the class ?"))
	return CountStudents

#3. input number of courses :
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses

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