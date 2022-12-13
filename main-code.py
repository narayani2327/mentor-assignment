from operator import attrgetter

class Mentor:
    def __init__(self,name, department, experience, subject):
        self.name=name
        self.department=department
        self.experience=experience
        self.subject=subject
    def display(self):
        print("Mentor details")
        print("Name",self.name)
        print("Subject",self.subject)
        print("Department",self.department)
        print("Experience",self.experience)
class Student:
    def __init__(self,name, numberOfSubjects, marks,usn,year):
        self.name=name
        self.numberOfSubjects=numberOfSubjects
        self.marks=marks
        self.usn=usn
        self.year=year
    def display(self):
        print("Student details")
        print("Name",self.name)
        print("USN",self.usn)
        print("Year",self.year)
        print("Number of subjects",self.numberOfSubjects)
        for i in self.marks:
            i.display()
class Subject:
    def __init__(self, name, marks, subjectID, credit):
        self.name=name
        self.subjectID=subjectID
        self.credit=credit
        self.mark=marks
    def display(self):
        print("Subject details")
        print("Name",self.name)
        print("Subject ID",self.subjectID)
        print("Credits",self.credit)
        print("Marks",self.mark)
    
print("-----------Welcome to Mentor assignment program-----------")
numberOfStudents=int(input("Please enter the number of students -- "))
numberOfMentors=int(input("Please enter the number of mentors -- "))
mentors=[]
students=[]
print("Please enter mentor details")
for i in range(numberOfMentors):
    print("\nMentor",i+1, "details")
    name=input("Enter name ")
    department=input("Enter department ")
    experience=input("Enter experience ")
    subject=input("Enter subject ")
    m = Mentor(name, department, experience, subject)
    mentors.append(m)

print("Please enter students details")
for i in range(numberOfStudents):
    print("\nStudent",i+1, "details")
    name=input("Enter name ")
    usn=input("Enter usn ")
    year=input("Enter year ")
    numberOfSubjects=int(input("Enter number of subjects "))
    sub=[]
    for j in range(numberOfSubjects):
        print("Subject",j+1, "details")
        subjectName=input("Enter subject name ")
        subjectID=input("Enter subjectID ")
        credit=input("Enter credits ")
        marks=input("Enter marks ")
        s= Subject(subjectName, marks, subjectID, credit)
        sub.append(s)
    st = Student(name, numberOfSubjects, sub, usn, year)
    students.append(st)


# for i in students:
#     i.display()
# for i in mentors:
#     i.display()



for i in students:
    max_attr = min(i.marks, key=attrgetter('mark'))
    print(max_attr.mark, max_attr.name)
    mento=[]
    for j in mentors:
        if j.subject==max_attr.name:
            mento.append(j)
    if len(mento)>1:
        print(max(mento.experience))
    else:
        print(mento[0].name)
