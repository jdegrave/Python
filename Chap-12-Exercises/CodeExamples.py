class Person:
    def getInfo(self):
        return "Person"
    def printPerson(self):
        print(self.getInfo())


class Student(Person):
    def getInfo(self):
        return "Student"

Person().printPerson()
Student().printPerson()