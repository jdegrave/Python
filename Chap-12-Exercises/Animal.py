class Animal():
    def __init__(self):
        pass

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self):
        pass
    def make_sound(self):
        pass


class Bird(Animal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        pass
class Insect(Animal):
    def make_sound(self):
        pass


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Bark!")

class Cat(Mammal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Meow!")

class Wolf(Mammal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Howl!")

class Human(Mammal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Who's your daddy?")

class Goat(Mammal):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print ("Bleat!")

class Goose(Bird):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Honk!")
class Parrot(Bird):
    def __init__(self):
        super().__init__()
        pass

    def make_sound(self):
        print("Squawk!")


class Cricket(Insect):
    def __init__(self):
        super().__init__()
        pass


    def make_sound(self):
        print("Chirp!")


class Cicada(Insect):
    def __init__(self):
        super().__init__()
        pass

    def make_sound(self):
        print("Shhhzzzh!")


class Fly(Insect):
    def __init__(self):
        super().__init__()
        pass
    def make_sound(self):
        print("Buzz!")


class Mosquito(Insect):
    def __init__(self):
        super().__init__()
        pass

    def make_sound(self):
        print("Zzzzzzzzzz!")


def main():

    fluffy = Cat()
    fido = Dog()
    polly = Parrot()
    jerky_fly = Fly()
    super_cicada = Cicada()
    zika = Mosquito()
    jiminy = Cricket()
    alfred = Goat()
    lobo = Wolf()
    christmas = Goose()
    eve = Human()

    zoo = [fluffy, fido, polly, jerky_fly, super_cicada, zika, jiminy, alfred, lobo, christmas, eve]

    for i in range(len(zoo)):
        zoo[i].make_sound()


main()





