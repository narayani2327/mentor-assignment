from operator import attrgetter

class Mentor:
    def __init__(self,name, department, experience, subject):
        self.name=name
        self.department=department
        self.experience=experience
        self.subject=subject
    def display(self):
        print("\nName:",self.name,end="")
        print("Subject:",self.subject,end="")
        print("Department:",self.department,end="")
        print("Experience:",self.experience,end="")

class Student:
    def __init__(self,name, numberOfSubjects, marks,usn,year):
        self.name=name
        self.numberOfSubjects=numberOfSubjects
        self.marks=marks
        self.usn=usn
        self.year=year
    def display(self):
        print("=======================")
        print("Name:",self.name,end="")
        print("USN:",self.usn,end="")
        print("Year:",self.year,end="")
        print("Number of subjects:",self.numberOfSubjects,end="")
        for i in self.marks:
            i.display()

class Subject:
    def __init__(self, name, marks, subjectID, credit):
        self.name=name
        self.subjectID=subjectID
        self.credit=credit
        self.mark=marks
    def display(self):
        print("\nSubject details")
        print("Name:",self.name,end="")
        print("Subject ID:",self.subjectID,end="")
        print("Credits:",self.credit,end="")
        print("Marks:",self.mark,end="")
    
print("-----------Welcome to Mentor assignment program-----------")
mentors=[]
students=[]
with open("mentor-data.txt") as fp:
    print("\n---------Mentor details---------")
    while True:
        name=fp.readline()
        department=fp.readline()
        experience=fp.readline()
        subject=fp.readline()
        if not name:
            break
        m = Mentor(name, department, experience, subject)
        m.display()    
        mentors.append(m)


with open("student-data.txt") as fp:
    print("\n\n---------Student details---------")
    while True:
        name=fp.readline()
        usn=fp.readline()
        year=fp.readline()
        numberOfSubjects=fp.readline()
        if not name:
            break
        sub=[]
        for j in range(int(numberOfSubjects)):
            subjectName=fp.readline()
            subjectID=fp.readline()
            credit=fp.readline()
            marks=fp.readline()
            s= Subject(subjectName, marks, subjectID, credit)
            sub.append(s)
        st = Student(name, numberOfSubjects, sub, usn, year)
        students.append(st)
        st.display()

print("\n\n=======Mentor allocation=======")
for i in students:
    max_attr = min(i.marks, key=attrgetter('mark'))
    mento=""
    maxExp=0
    for j in mentors:
        if j.subject==max_attr.name and int(j.experience)>int(maxExp):
            mento=j.name
            maxExp=j.experience
    print("Student name:",i.name,end="")
    print("Mentor assigned:",mento,end="")
    print("Marks obtained:",max_attr.mark,end="")
    print("Subject Name:",max_attr.name)