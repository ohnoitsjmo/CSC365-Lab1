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
                self.student(last_name)
    
    def student(self, last_name):
        print(last_name)

    # def teacher():

    # def bus():

    # def grade():

    # def average():

    # def info():

    # def quit():

s = SchoolSearch()
s.main()