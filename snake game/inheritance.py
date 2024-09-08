class Animal:
    def __init__(self) -> None:
        self.eyes=2
        
    def breathe(self):
        print("breathing")

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def meow(self):
        print("meow")

cat1=Cat()
print(cat1.eyes)
cat1.breathe()
cat1.meow()


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("swimming")



fish1=Fish()
print(fish1.eyes)
fish1.breathe()
fish1.swim()