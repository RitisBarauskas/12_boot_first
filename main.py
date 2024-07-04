

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


def main():
    john = Human("John", 30)
    bill = Human("Bill", 25)
    maxim = Human("Max", 35)

    students = [john, bill, maxim]

    for student in students:
        student.say_hello()


if __name__ == "__main__":
    main()
