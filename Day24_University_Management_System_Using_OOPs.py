'''
                                UNIVERSITY MANAGEMENT SYSTEM USING OOPS
                                ---------------------------------------



'''

class Person:
    university_name = "Codegnan University"   # Class Attribute

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Student ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course, Year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.Year_ = Year_

        Student.student_count += 1

    def display_info(self):
        print("\n------ Student Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.__student_id)
        print("Course     :", self.course)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :", cls.student_count)


# ---------------- Faculty ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Faculty ID :", self.__faculty_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :", cls.faculty_count)

# ---------------- Non-Teaching Staff ---------------- #

class NonTeachingStaff(Person):
    nonTeachingStaff_count = 0
    def __init__(self, name, age, staff_id, gender, education, department, designation):
        super().__init__(name, age, education, gender, department)
        self.__staff_id = staff_id
        self.designation = designation

        NonTeachingStaff.nonTeachingStaff_count += 1

    def display_info(self):
        print("\n----------Non Teaching staff----------")
        print("University:", Person.university_name)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Staff ID:", self.__staff_id)
        print("Edu_BG:", self.Edu_BG)
        print("Department:",self.Department)
        print("Designation:",self.designation)
    def get_staff_id(self):
        return self.__staff_id
    @classmethod
    def total_staff(cls):
        print("Total Non-Teaching staff:", cls.nonTeachingStaff_count)

    @staticmethod
    def office_rules():
        print("\nOffice Rules")
        print("Working Hours: 9:00 AM - 5:00 PM")


# ---------------- Objects ---------------- #

student1 = Student("Rahul Sharma",21,"CNU12345","Computer Science",2026,"Intermediate","Male","IT")

student2 = Student("Ananya Reddy",22,"CNU67890","Data Science",2026,"Intermediate","Female","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45,"F001","AI & ML","PhD","Male")

faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","Cybersecurity","PhD","Female")

nonTeachingStaff1 = NonTeachingStaff("Suresh", 40, "CDN001", "Male", "B.Sc", "Computer Lab", "Lab Assistant")

# ---------------- Output ---------------- #

student1.display_info()
student2.display_info()

print("\nStudent ID:", student1.get_student_id())

faculty1.display_info()
faculty2.display_info()

Faculty.university_policy()

nonTeachingStaff1.display_info()
print("\nStaff ID:", nonTeachingStaff1.get_staff_id())


Student.total_students()
Faculty.total_faculty()
NonTeachingStaff.total_staff()







        

    
        
    


















