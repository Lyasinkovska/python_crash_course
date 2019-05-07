class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += int(increase)
        print(self.first +" " + self.last + ": annual salary " + str(self.salary))

me = Employee("Liuda", "Yasinkovska", 10000)
me.give_raise(9000)