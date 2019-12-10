class Person:

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def sleep(self):

        print("Person need sleep")

    def eat(self):

        print("Person need eat")


class Student(Person):

    def __init__(self,name,sex,age,score):
        super(Student, self).__init__(name,sex,age)
        self.score = score

    def sleep(self):
        print("it is impossible")

    def eat(self):
        print("you need study")


class Teacher(Person):
    def __init__(self,name,sex,age,free):
        super(Teacher, self).__init__(name, sex, age)
        self.free = free

    def sleep(self):
        print("sleepping")

    def eat(self):
        print("the life is very good!")


if __name__ == '__main__':
    person = Person("彭达", "男", 20)
    person.eat()
    person.sleep()

    student = Student("pengda","nan",20,99)
    student.sleep()
    student.eat()

    teacher = Teacher("dada","男", 19,10000000)
    teacher.eat()
    teacher.sleep()