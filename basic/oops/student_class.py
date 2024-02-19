class Student:

    # class variable
    school_name = "KV"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private_school_no = 10

    # instance method
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_private_school_no(self):
        return self.__private_school_no

    def set_name(self, nm):
        self.name = nm

    def set_age(self, ag):
        self.age = ag

    @classmethod
    def get_school_name(cls):
        print("Class method called")
        print("Class variable:", cls.school_name)

    @staticmethod
    def my_static_hello():
        print("Hello World")


if __name__ == "__main__":
    print(Student.my_static_hello())

    s1 = Student("satya", 31)
    s2 = Student("swati", 28)

    print(s1.get_name(), s1.get_age(), s1.get_private_school_no())
    s1.set_name("sat")
    print(s1.get_name(), s1.get_age())

    Student.school_name = "DAV"
    print(Student.get_school_name())
    print(s2.get_name(), s2.get_age(), s2.school_name)
