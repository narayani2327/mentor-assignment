class Mentor:
    def __init__(self,name, department, experience, subject):
        self.name=name
        self.department=department
        self.experience=experience
        self.subject=subject
    def __str__(self):
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
        print("Number of subjects",self.numberOfSubjects)
        print("Marks",self.marks)
        print("USN",self.usn)
        print("Year",self.year)
class Subject:
    def __init__(self, name, marks, subjectID, credits):
        self.name=name
        self.subjectID=subjectID
        self.credits=credits
        self.mark=marks