class User():

    def __init__(self, first_name, last_name, age = "", occupation = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.occupation)

    def greet_user(self):
        print("Hello "+ self.first_name + " " + self.last_name)


'''me = User("Liuda", "Yasinkovska", "28")
me.describe_user()
me.greet_user()

he = User("Yura", "Mamonov", "36", "frontend developer")
he.describe_user()
he.greet_user()

she = User("Dashka", "Mamonova")
she.describe_user()
she.greet_user()'''