from operator import itemgetter, attrgetter, methodcaller


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    # def __str__(self):
    #     return print(self.name, self.grade, self.age)


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'C', 12),
    Student('dave', 'B', 10),
]

# print(student_objects)
# 按年龄排序
# s1 = sorted(student_objects, key=lambda student: student.age)
# print(s1)
# # 先按年级排序，再按年龄排序
s2 = sorted(student_objects, key=attrgetter('grade', 'age'))
print(s2)
#
# l = [1, 4, 3, 2, 9, 8, 6, 7, 5]
# l.sort(key=itemgetter(1))
# print(l)