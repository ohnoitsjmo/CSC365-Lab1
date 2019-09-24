import re

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
            if self.is_command_type("Student",command):
                self.student(command, _dict)
            elif self.is_command_type("Teacher",command):
                self.teacher(command, _dict)
            elif self.is_command_type("Bus",command):
                self.bus(command,_dict)
            elif self.is_command_type("Grade",command) :
                self.grade(command,_dict)
            elif self.is_command_type("Average",command):
                self.average(command, _dict)
            elif command == "Info" or command == "I":
                self.info(_dict)
            # if user want to quit
            # print Goodbye and stop program
            elif command == "Q" or command == "Quit":
                self.quit()
                return
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
                
    def is_command_type(self,command_type_string,command):
        if command_type_string + ": " in command or command_type_string[0] + ": " in command:
            return True
        return False

    def bus(self,bus_command,_dict):
        bus_num = re.search(r'\d+', bus_command).group()
        for item in _dict:
            if(_dict[item].Bus == bus_num):
                print (_dict[item].StFirstName + " " + 
                  _dict[item].StLastName + " " + _dict[item].Grade + 
                  " " + _dict[item].Classroom + "\n")

    def grade(self,grade_command,_dict):
        grade_number = re.search(r'\d+', grade_command).group()
        if " High" in grade_command or " H" in grade_command:
            highest = _dict[0]
            for item in _dict:
                if(_dict[item].Grade == grade_number and 
                    _dict[item].GPA > highest.GPA):
                  highest = _dict[item]
            if highest.Grade == grade_number:
                print (highest.StFirstName + " " + highest.StLastName)
            return
        elif " Low" in grade_command or " L" in grade_command:
            lowest = _dict[0]
            for item in _dict:
                if(_dict[item].Grade == grade_number and 
                    _dict[item].GPA < lowest.GPA):
                  lowest = _dict[item]
            if lowest.Grade == grade_number:
                print (lowest.StFirstName + " " + lowest.StLastName)
            return
        for item in _dict:
                if(_dict[item].Grade == grade_number):
                    print (_dict[item].StFirstName + " " + 
                      _dict[item].StLastName + "\n")

    def average(self, grade_value, _dict):
        # if no students in database
        # do nothing and return
        if len(_dict) == 0:
            return
        # create list to save students GPA
        # if found students have given grade
        selected_students = []
        # for each student
        for student in _dict.values():
            # check if student's grade equal to given grade
            # if so, convert student's GPA to float and add to the list
            try:
                if student.Grade == grade_value:
                    selected_students.append(float(student.GPA))
            # in the case of error (GPA is not a number)
            # return
            except ValueError:
                return
        # if students with given grade were found
        # compute average gpa and print message
        if selected_students:
            average_gpa = sum(selected_students) / len(selected_students)
            print("Grade: {}".format(grade_value))
            print("GPA: {}".format(average_gpa))
        # in other case return
        else:
            return

    def info(self, _dict):
        # if no students in database
        # do nothing and return
        if len(_dict) == 0:
            return
            # create dictionary-counter with keys - grade (0-6)
        # and values counts of students which have given grade
        grades_dict = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }
        # for every student
        # take grade and increase appropriate value of dict-counter by 1
        for student in _dict.values():
            grades_dict[student.Grade] += 1
        # print results
        for key in sorted(grades_dict.keys()):
            print("Grade {}: {}".format(key, grades_dict[key]))

    def quit(self):
        # print goodbye message
        print("Goodbye!")

s = SchoolSearch()
s.main()