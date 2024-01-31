from threading import Thread
from datetime import datetime
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
        if self.Hhungry > 30000000:
            self.state = "DEAD"
            print(self.Hhungry)

    def running(self):
        print(f"{self.nome} is running")
        self.motion = "running"
        while self.motion != "stopped":
            self.run()
            if self.state == "DEAD":
                self.stop()
            sleep(0.1)
    def stop(self):
        self.motion = "stopped"
        #print(f"{self.nome} is {self.motion}")

class Dog(Animals):
    def __init__(self, nome) -> None:
        super().__init__(nome)



def main():
    before = datetime.now()

    dog1 = Dog("scooby")
    print(dog1.nome)
    print(dog1.Hhungry)

    # 'running' in a separate thread
    running_thread = Thread(target=dog1.running)
    running_thread.start()

    #'stop' from the main thread
    running_thread.join()
    #dog1.stop()
    print(dog1.Hhungry)

    after = datetime.now()
    print(after - before)

if __name__ == "__main__":
    main()  