from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email
    
    def get_name(self):
            return self._name

    def set_name(self,name):
            self._name = name

    def get_age(self):
            return self._age

    def set_age(self,age):
            self._age = age

    def get_email(self):
            return self._email

    def set_email(self,email):
            self._email = email
    @abstractmethod    
    def get_role(self):
        pass
class Student(Person):
    def __init__(self, name, age, email):
        Person.__init__(self, name, age, email)
        self._grades = []

    def add_grade(self,grade):
        self._grades.append(grade)
        
    def calculate_average(self):
        return sum(self._grades)/len(self._grades)

        
    def get_status(self):
        average = self.calculate_average()
        return "Pass" if average >= 70 else "Fail"
            
    def get_role(self):
            return 'Student'
class Instructor(Person):
    def __init__(self, name, age, email, subject):
        Person.__init__(self, name, age, email)
        self._subject = subject

    def assign_grade(self,student,grade):
        student.add_grade(grade)
        
    def get_role(self):
            return 'Instructor'

class Course:
    def __init__(self, course_name):
        self._course_name = course_name
        self._students = []
        self._instructor = None

    def add_students(self,student):
        self._students.append(student)

    def set_instructor(self,instructor):
        self._instructor = instructor
    
    def generate_report(self):
        print(f"Course: {self._course_name}")
        if self._instructor:
            print(f"Instructor: {self._instructor.get_name()} ({self._instructor.get_email()})")
        else:
            print("No instructor assigned.")

        print("Students:")
        for student in self._students:
            average = student.calculate_average()
            status = student.get_status()
            print(f"- {student.get_name()} (Email: {student.get_email()}): Average = {average:.2f}, Status = {status}")
            
def print_person_info(person):
    print(f"Name: {person.get_name()}, Role: {person.get_role()}, Email: {person.get_email()}")

#Object
student1 = Student("Tanvi", 21, "Tanvi@gmail.com")
student2 = Student("Bob", 18, "Bob12@gmail.com")
instructor1 = Instructor("Dr.Smith", 35, "Smith1@gmail.com", "Math")

course = Course("Intro to Geometry")
course.add_students(student1)
course.add_students(student2)
course.set_instructor(instructor1)

instructor1.assign_grade(student1, 80)
instructor1.assign_grade(student1, 74)
instructor1.assign_grade(student2, 45)
instructor1.assign_grade(student2, 92)

course.generate_report()

print("\n")
for person in [student1, student2, instructor1]:
    print_person_info(person)
