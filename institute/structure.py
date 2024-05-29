"""this module defines the basic structures necessary
"""
class Course:
    """ this repracents cource
    """
    def__init__(self, course_id:str, name:str) -> None:
        self.course_id = course_id
        self.name = name
    
    @property
    def name(self):
        """this property represents name
        """
        return self._name
    @property
    def course_id(self):
        """ this property represents course
        """ 
        return self._course_id
    
class Student:
    """ this represents student
    """
    def__init__(self, name:str, age:int) -> None:
        self.student_id = student_id
        self.name = name
        self.courses = []
        
    def enroll_course(self, course:Course):
        """ we are 