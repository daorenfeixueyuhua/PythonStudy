class Programer:
    hobby = "Play Computer"

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight
    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print("My name is %s\nI am %s years old\n" %(self.name, self._age))


if __name__ == '__main__':

    programer = Programer("pengda", 20, 55)
    print(programer)
    # 返回 属性名：值 形式
    print(programer.__dict__)

    print(programer.get_weight)
    print(Programer.get_hobby())
    programer.self_introduction()
