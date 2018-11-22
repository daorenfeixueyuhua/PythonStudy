class OldStyle:
    def __init__(self, name):
        self.name = name


class NewStyle(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    old = OldStyle("old")
    # print(old.type())
    print(old.__dir__())
    print("-----------------------------")
    new = NewStyle("new")
    print(new.__dir__())

