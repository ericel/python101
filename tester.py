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
    print(t_students_grades)
    for student, grade in t_students_grades:
        print(student, '  | ',  grade)
#matchStudentsGradesSets()

"""
Test for files
"""
"""
try:
    countries = open('countries.txt')
    for country in countries:
        print(country)
    countries.close()
except Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)    
"""
"""
import os
try:
    homefiles = os.listdir('/home')
    print(homefiles)
except  Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)  


try:
    files_dir = open('files')
    print(files_dir)
except  Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)      

import os 

def find_file(a):
    b = os.getcwd()
    for direct, subdir, name in os.walk(b):
        for fname in name: 
            if fname == a:
                return os.path.join(direct, a)


file2read = "words.txt"
try: 
    fin = open(file2read)
    read = fin.readline()
    print(read)
except: 
    fin2 = find_file(file2read)
    fina = open(fin2)
    read2 = fina.readline()
    print(read2)
 
try: 
    fin = open("quick_brown.txt")
    for country in fin:
        print(country)
    countries.close()
except: 
    fin = open("quick_brown.txt", "w")
    fin.write("The quick brown fox jumps over the lazy dog.")
    fin.close()
 """
try:
    countries = open('countries.txt')
    for country in countries:
        print(country)
    countries.close()
except Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)
import os
try:
    homefiles = os.listdir('/home')
    print(homefiles)
except  Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)  


try:
    files_dir = open('files')
    print(files_dir)
except  Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)      


try:
    example3= open ('quick_brown.txt','r')
    pop=example3.write('add this line')

except Exception as err:
    print(type(err))    # the exception type
  
    print(err)
    
try:
    fin = open('answer.txt')
    fin.write('Yes')
except:
    print('No')
print('Maybe')
