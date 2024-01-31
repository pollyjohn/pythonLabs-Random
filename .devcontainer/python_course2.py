from datetime import datetime
from time import sleep
import asyncio
import os


class Animals:
    def __init__(self, nome, Hhungry = 0, Isound = '', state = 'alive', motion = 'stopped') -> None:
        self.nome = nome
        self.Hhungry = Hhungry
        self.Isound = Isound
        self.state = state
        self.motion = motion
        
    def sound(self, Isound:str):
        self.Isound = Isound

    def hungry(self, Hhungry:int):
        self.Hhungry = Hhungry 

    async def run(self):
        self.Hhungry += 2
        if self.Hhungry > 30000000000:
            self.state = "DEAD"
        else:
            pass
    async def running(self):
        self.motion = "running"
        print(f"{self.nome} is running")
        
        while self.motion == "running":
            await self.run()
            if self.state == "DEAD":
                return await self.stop()
        print(f"{self.nome} is stopped")    
    async def stop(self):
        self.motion = "stopped"
        print(f"{self.nome} is {self.motion}")
        return self.motion
    
    async def check_for_stop_command(self, file_path):
        while self.motion == 'running':
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    command = file.read().strip()
                    if command == 'stop':
                        await self.stop()
                        
            else:
                print("don't exist")
            await asyncio.sleep(1)

class Dog(Animals):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        

async def main():
    before = datetime.now() 
    dog1 = Dog("scooby")
    running_task = asyncio.create_task(dog1.running())
    await asyncio.sleep(6)
    command_task = asyncio.create_task(dog1.check_for_stop_command('command.txt'))

    await running_task
    await command_task
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

import asyncio

async def async_operation1():
    print('awaited 6 sec')
    await asyncio.sleep(6)
    print("backlog")
async def async_operation():
    print("Start of async operation")
      # Simulating an asynchronous operation (e.g., network request)
    print("done")
    print("End of async operation")
async def main():
    print("Before async operation")
    await async_operation()
    await async_operation1()
    print("After async operation")

# Run the event loop with the main coroutine
asyncio.run(main())
