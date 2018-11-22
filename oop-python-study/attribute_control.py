# 类的属性控制
class Programer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        print("getattribute", item)
        return super(Programer, self).__getattribute__(item)

    def __setattr__(self, key, value):
        print("setattr", key, value)
        self.__dict__[key] = value


if __name__ == '__main__':
    p = Programer("pengda",20)
    print(p.name)