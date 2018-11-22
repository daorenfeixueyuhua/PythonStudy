class Programer:
    body = "Play Computer"

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':

    programer = Programer("pengda", 20, 55)
    print(programer)
    # 返回 属性名：值 形式
    print(programer.__dict__)\

    print(programer.get_weight())
    print(programer._age)
    print(programer._Programer__weight)
    # print(programer.__weight) 访问失败