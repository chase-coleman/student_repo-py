# import re
grade_list = ['9th', '10th', '11th', '12th']
class Student:
    def __init__(self, name, age=12, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade
    
    def __repr__(self):
        return f"Student 1: {self._name}, Age: {self._age}, Grade {self._grade}."
        
    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 3:
            self._name = new_name
        else:
            print("Invalid name format.") 
    @property
    def age(self):
        return self._age
    @age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and (new_age in range(12, 18)):
            self._age = new_age
        else:
            print("invalid age value.")
    @property
    def get_grade(self):
        return self.grade
    @get_grade.setter
    def set_grade(self, new_grade):
        # bool(re.match(r"^(9th|10th|11th|12th)$", stu_grade)) == True
        if isinstance(new_grade, str) and new_grade in grade_list:
            self._grade = new_grade
    
    def advance(self):
        current_grade_index = grade_list.index(self.get_grade)
        if current_grade_index == 3:
            return "Chase has graduated!"
        else:
            return f"{self.get_name} has advanced to the {grade_list[current_grade_index+1]} grade"
    
    def study(self):
        return f"{self.get_name} is studying Computer Science"


student = Student("Chase", 26, '11th')
print(student.name) # Chase
# # student.set_name = "John"
# # print(student.get_name) # John
# # print(student.get_age) # 26
# # student.set_age = 18
# # print(student.get_age) #15
# # print(student.get_grade)  # 12th
# # student.set_grade = '11th'
# # print(student.get_grade) # 11th
# # print(student.advance())
# # print(student.study())
