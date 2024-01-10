import math


class Animal:
    """
    在python中使用__init__可以理解为js中的constructor构造方法
    注意:在Python中类的方法的第一个参数始终是self
    """

    def __init__(self, name):
        self.name = name

    """
    使用staticmethod装饰器时，可以不用cls这个参数，效果和classmethod + cls效果是一样的    
    """

    @staticmethod
    def create_animal(r):
        return Animal(r)

    """
    如果使用了classmethod装饰器，可以理解为该类的静态方法类似于使用static标记的方法。可以直接以类.方法名形式调用
    """

    @classmethod
    def static_method(cls):
        print(f'static_method print')

    "正常的类的方法写法"

    def say(self):
        print(f'my nam is {self.name}')


class Dog(Animal):

    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def say(self):
        super().say()
        print(f'i am {self.type}')


if __name__ == "__main__":
    m = Animal.create_animal("tom")
    print(m.name)
    # python中实例化一个类，不需要使用new，直接使用类名()即可进行实例化
    c = Animal("lucy")
    print(c.say())

    dog = Dog('Jams', 'dog')
    dog.say()
