from time import sleep

class Animals:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.Hhungry = 0
        self.Isound = ""
        self.state = "alive"
        self.motion = 'stopped'

    def sound(self, Isound:str):
        self.Isound = Isound

    def hungry(self, Hhungry:int):
        self.Hhungry = Hhungry 

    def run(self):
        self.Hhungry += 2
        if self.Hhungry > 10:
            self.state = "DEAD"
        else:
            pass
    def running(self):
        print(f"{self.nome} is running")
        while True:
            self.run()
            if self.state == "DEAD":
                return self.stop()
            elif self.stop() == 'stopped':
                break
            
    def stop(self):
        self.motion = "stopped"
        print(f"{self.nome} is {self.motion}")
        return self.motion 
        
class Dog(Animals):
    def __init__(self, nome) -> None:
        super().__init__(nome)

dog1 = Dog("scooby")
print(dog1.nome)
dog1.run()
print(dog1.Hhungry)
dog1.hungry(1)
dog1.sound("bark")
print(dog1.Hhungry)
dog1.run()
print(dog1.Hhungry)
print(dog1.Isound)
print(dog1.state)


dog2 = Dog("kripto")
dog2.run()
print(dog2.Hhungry)

dog2.sound("bark")
print(dog2.Hhungry)
dog2.run()
print(dog2.Hhungry)
print(dog2.Isound)
print(dog2.state)
