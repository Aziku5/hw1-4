from homework4 import A,B,C,D
class ABCD(A,B,C,D):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age
    @property
    def age(self):
        return self.__age

object = ABCD("Sam", 27)
print(object.name)
print(object.age)
object.method1()
object.method2()