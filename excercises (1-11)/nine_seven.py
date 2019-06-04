from nine_three import User
from nine_eight import Privileges

class Admin(User):

    def __init__(self, first_name, last_name, age = "", occupation = ""):
        super(Admin, self).__init__(first_name, last_name, age, occupation)
        self.pr = Privileges()





my_user = Admin("Liuda", "Yasinkovska")
my_user.greet_user()
print(my_user.pr.privileges)
