# LIBRARIES
from collections import namedtuple
from unidecode import unidecode
import csv

# CONSTANTS AND GLOBAL VARIABLES
NAMES_FILE = "data/names.txt"
SURNAMES_FILE = "data/surnames.txt"
STUDENT_NAMES_CSV = "data/fictitional-student-names.csv"
students = tuple()
unique_students = set([])
unique_ids = set([])

StudentId = namedtuple("StudentId", 
        [
            "Student", 
            "StudentNumber"
        ]
    )

# FUNCTION DEFINITIONS

def create_name_database(names_file, surnames_file):
    with open(names_file, 'r', encoding="utf-8") as f:
        names = f.readlines()
    
    with open(surnames_file, 'r', encoding="utf-8") as f:
        surnames = f.readlines()

    Student = namedtuple("Student", 
        [
            "Name", 
            "Surname"
        ]
    )
    global students
    for name, surname in zip(names, surnames):
        students += (Student(Name=name.replace('\n',''), Surname=surname.replace('\n','')),)
    
    return students

"""

"""
def create_myStudentNum(Name, Surname):
    vowels = set(['A', 'E', 'I', 'O', 'U'])

    id_name = ""
    id_sur = ""
    name_len = len(Name)
    surname_len = len(Surname)
    if name_len >= 3:
        id_name = Name[:3].upper()
    else:
        id_name = Name.upper()
        for i in range(3 - name_len):
            id_name += "X"

    surname = unidecode(Surname).upper().replace(" ","")
    for char in surname:
        if char in vowels:
            surname = surname.replace(char,"")
        
    if len(surname) >= 3:
        id_sur = surname[:3]
    else:
        id_sur = surname
        for i in range(3 - len(surname)):
            id_sur += "X"

    id_num_base = id_sur + id_name
    
    count = 1
    count_str = str(count).zfill(3)
    if(id_num_base+count_str) in unique_ids:
        while (id_num_base+count_str) in unique_ids:
            count += 1
            count_str = str(count).zfill(3)

    student_num = id_num_base+count_str
    unique_ids.add(student_num)
    student_entry = StudentId(Student=f"{Name} {Surname}", StudentNumber=student_num)
    unique_students.add( student_entry )
    
    return student_entry

def build_student_database():
    
    global students
    for student in students:
        create_myStudentNum(student.Name, student.Surname)

    with open(STUDENT_NAMES_CSV, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")

            writer.writerow(["Student", "StudentNumber"])

            global unique_students
            for entry in unique_students:
                writer.writerow([entry.Student, entry.StudentNumber])

# MAIN
def main():
    # prepare data
    # create_name_database(names_file=NAMES_FILE, surnames_file=SURNAMES_FILE)
    # build_student_database()  

    name = input("Please enter your first name: ")
    surname = input("Please enter your last name: ")  
    student_id = create_myStudentNum(name, surname)
    print(f"Your student number is {student_id.StudentNumber}")
# END OF MAIN

if __name__ == '__main__':
    main()