class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

student1 = student('jim', 'computer science', 3.4, True)
# student object

print(student1.gpa)
