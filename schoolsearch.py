class Student:
    def __init__(self, StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName):
        self.StLastName = StLastName
        self.StFirstName = StFirstName
        self.Grade = Grade
        self.Classroom = Classroom
        self.Bus = Bus
        self.GPA = GPA
        self.TLastName = TLastName
        self.TFirstName = TFirstName

class SchoolSearch:
    def main(self):
        command = input("Enter search command: ") 
        file = open("students.txt", "r")
        _dict = dict()
        i = 0
        for line in file:
            student = line.rstrip('\n').split(",")
            # Increment i and set student to respective index in dictionary
            _dict[i] = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7])
            i += 1

        while command != "Q" or command != "Quit":
            if command == "Student" or command == "S":
                last_name = input("Enter last name: ") 
                self.student(last_name, _dict)
            elif command == "Teacher" or command == "T":
                last_name = input("Enter last name: ") 
                self.teacher(last_name, _dict)
            command = input("Enter search command: ") 

    
    def student(self, last_name, _dict):
        inputs = last_name.split(" ")
        if len(inputs) == 1:
            for student in _dict.values():
                if student.StLastName == inputs[0]:
                    print("Student Last Name: {}".format(student.StLastName))
                    print("Student First Name: {}".format(student.StFirstName))
                    print("Grade: {}".format(student.Grade))
                    print("Classroom: {}".format(student.Classroom))
                    print("Teacher Last Name: {}".format(student.TLastName))
                    print("Teacher First Name: {}".format(student.TFirstName))
        elif len(inputs) == 2 and inputs[1] == "B" or inputs[1] == "Bus":
            for student in _dict.values():
                if student.StLastName == inputs[0]:
                    print("Student Last Name: {}".format(student.StLastName))
                    print("Student First Name: {}".format(student.StFirstName))
                    print("Bus Route: {}".format(student.Bus))  
                    

    def teacher(self, last_name, _dict):
        for student in _dict.values():
            if last_name == student.TLastName:
                print("Student Last Name: {}".format(student.StLastName))
                print("Student First Name: {}".format(student.StFirstName))
                
    # def bus():

    # def grade():

    # def average():

    # def info():

    # def quit():

s = SchoolSearch()
s.main()