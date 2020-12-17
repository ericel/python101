students = ('studentA', 'studentB', 'studentC');

unit_1 = [10, 5, 7]

unit_2 = [5, 9, 8]

unit_3 = [10, 5, 7]

unit_4 = [5, 6, 8]

unit_5 = [4, 5, 4]

unit_6 = [8, 8, 6]

unit_7 = [8, 9, 10]
sumAll = zip(students, unit_1, unit_2)

#print(list(sumAll))
# returns sum of each student's unit scores as a tuple
def sumAllUnits():
    return [sum(x) for x in zip(unit_1, unit_2, unit_3, unit_4, unit_5, unit_6, unit_7)]
# Matches students to sum of their units grades
def matchStudentGrades():
    grades = sumAllUnits()

    #list of tuples
    t_students_grades = zip(students, grades);
    
    for student, grade in t_students_grades:
        print(student, '  | ',  grade)

#matchStudentGrades()

list_units = [unit_1, unit_2, unit_3, unit_4, unit_5, unit_6, unit_7]

def matchStudentsGradesEnumerate():
    studentA = 0
    studentB = 0
    studentC = 0
    for i, grade in enumerate(list_units):
            studentA += grade[0]
            studentB += grade[1]
            studentC += grade[2]
    t_grades = [studentA, studentB, studentC]
    
    #list of tuples
    print(t_students_grades)
    t_students_grades = [(students[i],t_grades[i]) for i in range(0,len(students))]

    for student, grade in t_students_grades:
        print(student, '  | ',  grade)

#matchStudentsGradesEnumerate()


def sumAllUnits():
    return [sum(x) for x in zip(unit_1, unit_2, unit_3, unit_4, unit_5, unit_6, unit_7)]

def matchStudentsGradesSets():
    keys = students
    values = sumAllUnits()
    # Dictionary
    created_dict = {k: v for k, v in zip(keys, values)}
    #list of tuples
    t_students_grades = list(created_dict.items())

    for student, grade in t_students_grades:
        print(student, '  | ',  grade)
        
#matchStudentsGradesSets()

def test():
    """Stupid test function"""
    L = ()
    for i in range(100):
        L = L + (i,)
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
