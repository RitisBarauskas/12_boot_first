

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, num=1):
        print(f"{num}. Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Human(name={self.name}, age={self.age})"


def main():
    john = Human("John", 30)
    bill = Human("Bill", 25)
    maxim = Human("Max", 35)

    students = [john, bill, maxim]

    print('Hello from all students:')
    for num, student in enumerate(students, 1):
        student.say_hello(num)

    print('Students list:')
    for num, student in enumerate(students, 1):
        print(num, student)


if __name__ == "__main__":
    main()
