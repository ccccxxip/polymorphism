class Mood:
    def __init__(self, mood = "neurtal"):
        self.mood = mood
class Kindness(Mood):
    def be_kind(self):
        self.mood = "kind"
class Strictness(Mood):
    def be_strict(self):
        self.mood = "strict"

class Father(Strictness):
    def greet(self):
        return "Hello"

class Mother(Kindness):
    def greet(self):
        return "Hi, honey"
class Daughter(Kindness, Strictness):
    def greet(self):
        return "Hi, honey"
class Son(Father, Kindness):
    pass


father = Father()
mother = Mother()
daughter = Daughter()
son = Son()

print(father.greet())
print(mother.greet())
print(daughter.greet())
print(son.greet())

father.be_strict()
mother.be_kind()
daughter.be_strict()
son.be_kind()

print(father.mood)
print(mother.mood)
print(daughter.mood)
print(son.mood)
