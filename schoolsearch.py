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

class Teacher:
    def __init__(self, TLastName, TFirstName, Classroom):
        self.TLastName = TLastName
        self.TFirstName = TFirstName
        self.Classroom = Classroom

class SchoolSearch:
    def main(self):
        command = input("Enter search command: ") 
        students_file = open("list.txt", "r")
        teachers_file = open("teachers.txt", "r")
        _dict = dict()
        teacher_dict = dict()
        i = 0
        for line in students_file:
            student = line.rstrip('\n').split(",")
            # Increment i and set student to respective index in dictionary
            for _line in teachers_file:
                teacher = _line.rstrip('\n').split(",")
                if int(teacher[2]) == int(student[3]):
                    _dict[i] = Student(student[0], student[1], student[2], student[3], student[4], student[5], teacher[0], teacher[1])
                    teachers_file.seek(0)
                    break
            i += 1
        i = 0
        for line in teachers_file:
            teacher = line.rstrip('\n').split(",")
            teacher_dict[i] = Teacher(teacher[0], teacher[1], teacher[2])
            i += 1

        while command != "Q" or command != "Quit":
            isComment = command.startswith('#') or command.startswith("//")
            isAction = False
            if self.is_command_type("Student",command):
                self.student(command, _dict)
                isAction = True
            elif self.is_command_type("Teacher",command):
                self.teacher(command, _dict)
                isAction = True
            elif self.is_command_type("Classroom",command):
                self.classroom(command, _dict, teacher_dict)
                isAction = True
            elif self.is_command_type("Bus",command):
                self.bus(command,_dict)
                isAction = True
            elif self.is_command_type("Grade",command) :
                self.grade(command,_dict)
                isAction = True
            elif self.is_command_type("LamCommand",command) : #### block I added for N3
                self.LamCommand(_dict,teacher_dict)
                isAction = True
            elif ("Enrollment" == command) : #### block I added for N3
                self.enrollment(_dict,teacher_dict)
                isAction = True
            elif self.is_command_type("Average",command):
                self.average(command, _dict)
                isAction = True
            # command GPAv: <gpa number> H[igh]/L[ow] T[eacher]/B[us]/G[rade]
            elif self.is_command_type("GPAv", command):
                self.gpa(command, _dict)
                isAction = True
            elif command == "Info" or command == "I":
                self.info(_dict)
                isAction = True
            # if user want to quit
            # print Goodbye and stop program
            elif command == "Q" or command == "Quit":
                self.quit()
                students_file.close()
                teachers_file.close()
                return
            if (isComment):
                command = input("")
            elif(not isAction):
                command = input("\nEnter search command: ") 
            else:
                command = input("Enter search command: ") 
    
    # Given classroom, lists all students and all teachers in that classroom
    def classroom(self, command, _dict, teacher_dict):
        inputs = command.split(" ")
        for student in _dict.values():
            if int(student.Classroom) == int(inputs[1]):
                print(student.StLastName + "," + student.StFirstName)
        for teacher in teacher_dict.values():
            if int(teacher.Classroom) == int(inputs[1]):
                print(teacher.TLastName + "," + teacher.TFirstName)
    
    def gpa(self, command, _dict):
        # parse command, separate command, gpa, condition (low or high) and mode (bus, teacher or grade)
        try:
            command, gpa, condition, mode = command.split()
            gpa = float(gpa)
        except (IndexError, ValueError):
            print('')
            return
        students = []
        # get list of students according condition
        if condition == 'High' or condition == 'H':
            condition = 'High'
            # select all students with gpa equal or higher than gpa
            for student in _dict.values():
                if float(student.GPA) >= gpa:
                    students.append(student)
        elif condition == 'Low' or condition == 'L':
            condition = 'Low'
            # select all students with gpa equal or lower than gpa
            for student in _dict.values():
                if float(student.GPA) <= gpa:
                    students.append(student)
        # if condition was specified wrong, do nothing
        else:
            print('')
            return
        if not students:
            print('')
            return
            # if user wants to see teachers of selected students
        if mode == 'Teacher' or mode == 'T':
            # get all teachers of selected students
            teachers = [', '.join([student.TFirstName, student.TLastName]) for student in students]
            # create dictionary with keys - teacher names and values - number of students and student's names and grades
            # for example {'Marley, Bob': [2, [('Jones, Sara', '2', 'Smith, Simon', 3)]}
            counts = {}
            for i, teacher_ in enumerate(teachers):
                if teacher_ not in counts:
                    counts[teacher_] = [1, [
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade)]]
                else:
                    counts[teacher_][0] += 1
                    counts[teacher_][1].append(
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade))
            # print information
            # print gpa level
            print('GPA: {} and {}er'.format(gpa, condition))
            # sort teachers by number of students
            counts = sorted(list(counts.items()), reverse=True, key=lambda x: x[1])
            # print teacher's name and number of his students
            for count in counts:
                print('Teacher {}: {} students'.format(count[0], count[1][0]))
                # print students names and their grades
                for student in sorted(count[1][1], key=lambda x: x[1], reverse=True):
                    print('\tName: {}, grade: {}'.format(student[0], student[1]))
        # if user wants to see teachers of selected students
        elif mode == 'Bus' or mode == 'B':
            # get all buses of selected students
            buses = [student.Bus for student in students]
            # create dictionary with keys - bus number and values - number of students and student's names and grades
            # for example {'33': [2, [('Jones, Sara', '2', 'Smith, Simon', 3)]}
            counts = {}
            for i, bus_ in enumerate(buses):
                if bus_ not in counts:
                    counts[bus_] = [1, [
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade)]]
                else:
                    counts[bus_][0] += 1
                    counts[bus_][1].append(
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade))
            # print information
            # print gpa level
            print('GPA: {} and {}er'.format(gpa, condition))
            # sort buses by number of students
            counts = sorted(list(counts.items()), reverse=True, key=lambda x: x[1][0])
            # print bus and number of students
            for count in counts:
                print('Bus number {}: {} students'.format(count[0], count[1][0]))
                # print students names and their grades
                for student in sorted(count[1][1], key=lambda x: x[1], reverse=True):
                    print('\tName: {}, grade: {}'.format(student[0], student[1]))
        elif mode == 'Grade' or mode == 'G':
            try:
                grades_average = sum([float(student.Grade) for student in students]) / len(students)
            except ZeroDivisionError:
                print('')
                return
            # create dictionary with keys - gpa and values - number of students and student's names and grades
            # for example {'2.3': [2, [('Jones, Sara', '2', 'Smith, Simon', 3)]}
            counts = {}
            for i, student in enumerate(students):
                if student.GPA not in counts:
                    counts[student.GPA] = [1, [
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade)]]
                else:
                    counts[student.GPA][0] += 1
                    counts[student.GPA][1].append(
                        (', '.join([students[i].StLastName, students[i].StFirstName]), students[i].Grade))
            print('GPA: {} and {}er'.format(gpa, condition))
            print('Grade average: {}'.format(round(grades_average, 2)))
            # sort gpa by number of students
            counts = sorted(list(counts.items()), reverse=True, key=lambda x: x[0])
            # print gpa and number of students
            for count in counts:
                print('GPA {}: {} students'.format(count[0], count[1][0]))
                # print students names and their grades
                for student in sorted(count[1][1], key=lambda x: x[1], reverse=True):
                    print('\tName: {}, grade: {}'.format(student[0], student[1]))
        else:
            print()

    def student(self, command, _dict):
        inputs = command.split(" ")
        counter = 0
        if len(inputs) == 2:
            for student in _dict.values():
                if student.StLastName == inputs[1]:
                    counter+= 1
                    print (student.StLastName + "," + student.StFirstName + "," +
                        student.Grade + "," + student.Classroom + "," + student.TLastName + "," +
                        student.TFirstName)
        elif len(inputs) == 3 and inputs[2] == "B" or inputs[2] == "Bus":
            for student in _dict.values():
                if student.StLastName == inputs[1]:
                    counter+= 1
                    print(student.StLastName + "," + student.StFirstName + "," + student.Bus)
        if(counter == 0):
            print("")
                    
    def teacher(self, command, _dict):
        inputs = command.split(" ")
        counter = 0
        for student in _dict.values():
            if inputs[1] == student.TLastName:
                counter+= 1
                print(student.StLastName + "," + student.StFirstName)
        if(counter == 0):
            print("")
                
    def is_command_type(self,command_type_string,command):
        if command_type_string + ": " in command or command_type_string[0] + ": " in command:
            return True
        return False

    def bus(self,bus_command,_dict):
        bus_num = re.search(r'\d+', bus_command).group()
        counter = 0
        for item in _dict:
            if(_dict[item].Bus == bus_num):
                counter+= 1
                print (_dict[item].StFirstName + "," + 
                  _dict[item].StLastName + "," + _dict[item].Grade + 
                  "," + _dict[item].Classroom)
        if(counter == 0):
            print("")

    def grade(self,grade_command,_dict):
        grade_number = re.search(r'\d+', grade_command).group()
        counter = 0
        if " High" in grade_command or " H" in grade_command:
            highest = _dict[0]
            for item in _dict:
                if(_dict[item].Grade == grade_number and 
                    _dict[item].GPA > highest.GPA):
                  highest = _dict[item]
            if highest.Grade == grade_number:
                print (highest.StLastName + "," + highest.StFirstName)
            return
        elif " Low" in grade_command or " L" in grade_command:
            lowest = _dict[0]
            for item in _dict:
                if(_dict[item].Grade == grade_number and 
                    _dict[item].GPA < lowest.GPA):
                  lowest = _dict[item]
            if lowest.Grade == grade_number:
                print (lowest.StLastName + "," + lowest.StFirstName)
            return
        for item in _dict:
                if(_dict[item].Grade == grade_number):
                    counter+= 1
                    print (_dict[item].StLastName + "," + 
                      _dict[item].StFirstName)
        if(counter == 0):
            print("")

    def average(self, command, _dict):
        inputs = command.split(" ")
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
                if student.Grade == inputs[1]:
                    selected_students.append(float(student.GPA))
            # in the case of error (GPA is not a number)
            # return
            except ValueError:
                return
        # if students with given grade were found
        # compute average gpa and print message
        if selected_students:
            average_gpa = sum(selected_students) / len(selected_students)
            print(inputs[1] + "," + str(round(average_gpa,2)))
        # in other case return
        else:
            print()
            return

    def info(self, _dict):
        # if no students in database
        # do nothing and return
        if len(_dict) == 0:
            print("\n")
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

    def LamCommand(self,tgg_command,_dict,teacher_dict):
        grade_num = re.search(r'\d+', tgg_command).group()
        classroom_list = []
        for item in _dict:
            if (_dict[item].Classroom not in classroom_list):
                classroom_list.append(_dict[item].Classroom)
            else:
                pass
        for item in classroom_list:
            for ele in teacher_dict:
                if((int) (teacher_dict[ele].Classroom) == (int) (item)):
                    print (teacher_dict[ele].TLastName + "," +teacher_dict[ele].TFirstName)
                else: pass
    def enrollment(self,_dict,teacher_dict):
        print ("here")
        classroom_dict = dict()
        for student in _dict:
            if (((int) (_dict[student].Classroom)) not in classroom_dict):
                classroom_dict[((int)(_dict[student].Classroom))] = 0
            else: pass
            classroom_dict[((int)(_dict[student].Classroom))]+=1
        for i in sorted (classroom_dict) : 
            print(str(i) +"," + str(classroom_dict[i]))

    def quit(self):
        # print goodbye message
        print("Goodbye!")

s = SchoolSearch()
s.main()