from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, id, last_name, first_name, middle_name, birth_date, phone_number, address):
        self.id = int(id)
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.birth_date = str(birth_date)
        self.phone_number = str(phone_number)
        self.address = str(address)
    
    @abstractmethod
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
        
    @abstractmethod
    def get_age(self):
        pass


class Student(User):
    def __init__(self, id, last_name, first_name, middle_name, birth_date, phone_number, address, courses, tasks_solved, certificates):
        super().__init__(id, last_name, first_name, middle_name, birth_date, phone_number, address)
        self.courses = list(courses)
        self.tasks_solved = int(tasks_solved)
        self.certificates = list(certificates)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def get_age(self):
        return super().get_age()

    def get_courses_amount(self):
        pass

    def add_course(self):
        pass


class Teacher(User):
    def __init__(self, id, last_name, first_name, middle_name, birth_date, phone_number, address, education, beginning_of_work_experience, job):
        super().__init__(id, last_name, first_name, middle_name, birth_date, phone_number, address)
        self.education = str(education)
        self.beginning_of_work_experience = str(beginning_of_work_experience)
        self.job = str(job)
    
    def get_full_name(self):
        return super().get_full_name()
    
    def get_age(self):
        return super().get_age()
    
    def get_years_of_work_experience(self):
        pass

    def get_education_level(self):
        pass


class Course:
    def __init__(self, id, name, description, start_date, end_date, teacher, students, tasks):
        self.id = int(id)
        self.name = str(name)
        self.description = str(description)
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.teacher = str(teacher)
        self.students = list(students)
        self.tasks = list(tasks)

    def get_course_duration(self):
        pass

    def add_task(self):
        pass


class Task:
    def __init__(self, id, name, content, course, grade, solutions, correct_solutions):
        self.id = int(id)
        self.name = str(name)
        self.content = str(content)
        self.course = str(course)
        self.grade = int(grade)
        self.solutions = int(solutions)
        self.correct_solutions = int(correct_solutions)

    def get_success_statistics(self):
        pass

    def change_content(self):
        pass