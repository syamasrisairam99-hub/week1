class StudentProfile():
    def __init__(self,student_name,student_id,student_course,student_email,student_skills):
        self.student_name=student_name
        self.student_id=student_id
        self.student_course=student_course
        self.student_email=student_email
        self.student_skills=student_skills
    def shm(self):
        print("Student Name:", self.student_name)
        print("Student Id:", self.student_id)
        print("Student_course:", self.student_course)
        print("Student Email:", self.student_email)
        print("Student Skills:", self.student_skills)
st1=StudentProfile("Shyamu",4432,"python","syamasri@gmail.com",["Python","SQL","datascience"])
st2=StudentProfile("Harshi",4218,"python","harshi@gamil.com",["Python","Sql","AIML"])
st3=StudentProfile("Mani",4217,"Python","mani@gmail.com",["Python","Sql","AIML"])
st1.shm()
st2.shm()
st3.shm()
