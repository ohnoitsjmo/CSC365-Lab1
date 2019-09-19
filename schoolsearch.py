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
    def main():
        command = input("Enter search command: ") 
        file = open("students.txt", "r")
        _dict = dict()
        i = 0
        for line in file:
            student = line.rstrip('\n').split(",")
            # Increment i and set student to respective index in dictionary
            _dict[i] = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7])
            i += 1
        print(_dict.items())
    
        while command != "Q" or command != "Quit":
            if command == "Student" or command == "S":
                command = input("Enter search command: ") 
                student()
    
    def student():
        print("student")

    # def teacher():

    # def bus():

    # def grade():

    # def average():

    # def info():

    # def quit():

    if __name__ == "__main__":
        main()