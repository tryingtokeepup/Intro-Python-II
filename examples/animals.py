class Animal:
    def __init__(self, num_legs=4, animal_type="UNKNOWN", catchphrase="...."):
        self.type = animal_type
        self.num_legs = num_legs
        self.catchphrase = catchphrase
        self.is_flying = False

    def speak(self, phrase=None):
        if phrase is not None:
            print(phrase)
        else:
            print(self.catchphrase)

    def fly(self):
        print("You cannot fly.")


class Bird(Animal):
    def __init__(self):
        super().__init__(2, "bird", "Tweet")

    def fly(self):
        print("You flap your wings and hover in the air.")
        self.is_flying = False


class Cat(Animal):
    def __init__(self):
        self.type = "cat"
        self.num_legs = 4
        self.catchphrase = "meow!"


class Dog(Animal):
    def __init__(self):
        self.type = "dog"
        self.num_legs = 4
        self.catchphrase = "woof!"
