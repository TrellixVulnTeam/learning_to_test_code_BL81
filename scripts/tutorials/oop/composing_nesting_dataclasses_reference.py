# https://gist.github.com/ricky-lim/d4ab3ae470d331ead3875f22f6f0580f

#  Composing classes with dataclass, instead of deep-nested dictionary 
# From the book, effective python 2nd edition item 37


from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Grade:
    weight: int
    score: int


@dataclass
class Subject:
    grades: List[Grade] = field(default_factory=list)

    def report_grade(self, weight, score):
        grade = Grade(weight=weight, score=score)
        self.grades.append(grade)

    def average_grade(self):
        total_weight, total_count = 0, 0
        for grade in self.grades:
            total_count += grade.weight * grade.score
            total_weight += grade.weight
        return total_count / total_weight


@dataclass
class Student:
    subjects: Dict[str, Subject] = field(default_factory=lambda: defaultdict(Subject))

    def add_subject(self, subject):
        normalized_subject = subject.lower()
        return self.subjects[normalized_subject]

    def average_grade(self):
        total, count = 0, 0
        for subject in self.subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


@dataclass
class GradeBook:
    students: Dict[str, Student] = field(default_factory=lambda: defaultdict(Student))

    def add_student(self, name):
        normalized_name = name.lower()
        return self.students[normalized_name]


book = GradeBook()
albert = book.add_student('Albert Einstein')
math = albert.add_subject('Math')
math.report_grade(weight=0.05, score=75)
math.report_grade(weight=0.15, score=65)
math.report_grade(weight=0.80, score=70)
gym = albert.add_subject('Gym')
gym.report_grade(weight=0.40, score=100)
gym.report_grade(weight=0.60, score=85)
assert albert.average_grade() == 80.25
