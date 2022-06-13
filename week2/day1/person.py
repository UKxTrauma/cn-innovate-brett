# class Person():
#     def __init__(self, name):
#         self.name = name
#         self.age = None

# new_person = Person("Brett")
# new_person.age = 28

# print(new_person.name, new_person.age)

class Person():
    def __init__(self, age, profession, height, name):
        self.name = name
        self.age = age
        self.profession = profession
        self.height = height
    def set_hair(self, person_hair):
        self.hair = person_hair
    def get_hair(self):
        print(self.hair)

new_person_x = Person(28, "student", "5'8'", "Brett")

# print(new_person_x.profession)

