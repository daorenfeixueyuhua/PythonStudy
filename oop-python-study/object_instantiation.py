# 对象的实例化
class Programer:
    
    def __new__(cls, *args, **kwargs):
        print("call __new__ method")
        print(args)
        return super(Programer, cls).__new__(cls, *args,**kwargs)

    def __init__(self, name, age):
        print("call __init__ method")
        self.name = name
        self.age = age


if __name__ == '__main__':
    programer = Programer("pengda", 19)
    print(programer.__dict__)