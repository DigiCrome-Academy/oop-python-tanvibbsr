# Assignment Instructions
OOP Python Assignment: Data Science Student Management System
Assignment Instructions
Create a simple student management system for a data science course using Object-Oriented Programming principles. Your solution should demonstrate all four pillars of OOP: Encapsulation, Inheritance, Polymorphism, and Abstraction.

Requirements:
Create a base class Person with:
Private attributes: _name, _age, _email
Constructor to initialize these attributes
Getter and setter methods for each attribute
An abstract method get_role() that returns the person's role

Create a Student class that inherits from Person:
Additional private attribute: _grades (list of numerical grades)
Method add_grade(grade) to add a grade
Method calculate_average() to return average grade
Method get_status() that returns "Pass" if average ≥ 70, else "Fail"
Override get_role() to return "Student"

Create an Instructor class that inherits from Person:
Additional private attribute: _subject
Method assign_grade(student, grade) that adds a grade to a student
Override get_role() to return "Instructor"

Create a Course class with:
Private attributes: _course_name, _students (list), _instructor
Methods to add students and set instructor
Method generate_report() that prints course statistics

Demonstrate polymorphism by creating a function that works with any Person object

Test Your Implementation:
Create 2 students and 1 instructor
Create a course and add them to it
Have the instructor assign grades to students
Generate a course report