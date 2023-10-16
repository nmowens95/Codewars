# Title: These are not my grades!

# Instructions:
'''
At the end of the last semester, Prof. Joey Greenhorn implemented an online report card for his students in order to save paper. Everything seemed to be working fine back then, but since the start of the new semester he has received several emails from students complaining about erroneous grades showing up in their online report cards. Can you help him correct his implementation of the "Student" class?

The "Student" class should behave like this :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98] # Evaluates to True
someOtherStudent.grades == [77] # Evaluates to True
But right now, this is happening :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98, 77] # Evaluates to True
someOtherStudent.grades == [98, 77] # Evaluates to True
'''

# Answer:

class Student:

    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0

# Sample Tests:
'''
from solution import Student
import codewars_test as test

@test.describe("These are not my grades")
def these_are_not_my_grades():
    
    @test.it("Last semester. Everything was going fine.")
    def test_it():
        
        # Last semester
        # Everything is working fine, no angry emails
        matthewConnorGrades = [44, 53, 27, 60]
        chloeMadisonGrades = [79, 58, 30, 66]
        studentGrades = matthewConnorGrades, chloeMadisonGrades
        matthewConnor = Student('Matthew', 'Connor', matthewConnorGrades)
        chloeMadison = Student('Chloe', 'Madison', chloeMadisonGrades)
        students = matthewConnor, chloeMadison
        
        for i, student in enumerate(students):
            test.assert_equals(student.grades, studentGrades[i])
    
    @test.it("New semester. Something is wrong, can you fix it?")
    def test_it():
        
        # Very beginning of the semester
        # Initialize students so they can log in to the online report card
        johnDoe = Student('John', 'Doe')
        janeDoe = Student('Jane', 'Doe')
        jamesSmith = Student('James', 'Smith')
        jennaSmith = Student('Jenna', 'Smith')
        students = johnDoe, janeDoe, jamesSmith, jennaSmith
        
        # First graded assessment
        # Update students' grades so they can see them on the online report card
        firstAssessmentGrades = [63, 92, 82, 75]
        for i, student in enumerate(students):
            student.add_grade(firstAssessmentGrades[i])
        
        # And then the angry emails started coming in...
        for i, student in enumerate(students):
            test.assert_equals(student.grades[0], firstAssessmentGrades[i])
'''