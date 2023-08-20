# множественное наследование
# MRO - method resolution order порядок выполнения методов

class A:
    def __init__(self, a):
        self.a = a

    def c(self):
        print(self,'это метод А')


class A2(A):...


class C:
    def __init__(self, с):
        self.с = с

    def c1(self):
        print(self,'это метод C')



class B(A2,C,A):
    def __init__(self,a,c):
        A.__init__(self,a)
        C.__init__(self,c)




b=B('a','c')
b.c()
print(B.mro())

class Saving:...
class Real():...
class Bond:...
class Checking:...
class Stock:...
class Bank(Saving, Checking):...
class Secu(Bond, Stock):...
class Interest(Bank, Secu):...
class Insur(Real, Bank):...
class Asset(Real, Secu, Bank):...
print()






