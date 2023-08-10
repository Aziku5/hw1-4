from lesson1 import People, people2


# 4 принципы ооп - наследование - полимаорфизм инкапсуляция обстракция

class Student(People):  # дочерний класс

    def __init__(self, name, age, view):
        People.__init__(self, name, age)
        super().__init__(name, age)
        self.view = view

    def eating_fastfood(self):
        print(self.name, 'eating')

    def print(self):
        print('aaaaaaaaaaaa')


student1 = Student('beka', 20, 0)

student1.eating_fastfood()
student1.print()
people2.print()
People.print(student1)
# print(Student.mro())


class Teach(Student):
    def print(self):
        super().print()
        Student.print(self)
        People.print(self)

    def __str__(self):
        




beka = Teach('beka', 20, 0)

beka.print()
print(Teach.mro())

print(beka)



