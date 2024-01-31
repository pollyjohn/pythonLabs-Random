from datetime import datetime
from time import sleep
import asyncio

class Animals:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.Hhungry = 0
        self.Isound = ""
        self.state = "alive"
        self.motion = 'stopped'
        self.stop_event = asyncio.Event()

    def sound(self, Isound:str):
        self.Isound = Isound

    def hungry(self, Hhungry:int):
        self.Hhungry = Hhungry 

    async def run(self):
        self.Hhungry += 2
        if self.Hhungry > 3000000000:
            self.state = "DEAD"
        else:
            await asyncio.sleep(0.3) 
    
    async def running(self):
        print(f"{self.nome} is running")
        self.motion = "running"
        while self.motion != "stopped" and not self.stop_event.is_set():
            await self.run()
            if self.state == "DEAD":
                return await self.stop()
        print(f"{self.nome} is stopped")    
    
    async def stop(self):
        self.motion = "stopped"
        self.stop_event.set()
        print(f"{self.nome} is {self.motion}")

class Dog(Animals):
    def __init__(self, nome) -> None:
        super().__init__(nome)

async def main():
    before = datetime.now() 

    dog1 = Dog("scooby")

    print(dog1.nome)
    running_task = asyncio.create_task(dog1.running())  
    await asyncio.sleep(5)
    #other_task = asyncio.create_task(dog1.stop())
    await dog1.stop()
    await running_task
    #await other_task
    print(dog1.Hhungry)
    after = datetime.now()
    print(after-before)
asyncio.run(main())
#dog2 = Dog("kripto")
#dog2.run()
#print(dog2.Hhungry)

#dog2.sound("bark")
#print(dog2.Hhungry)
#dog2.run()
#print(dog2.Hhungry)
#print(dog2.Isound)
#print(dog2.state)