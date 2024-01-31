# using IPC method without asyncio. Only multi-threading


from datetime import datetime
from threading import Thread
from time import sleep

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

    def run(self):
        self.Hhungry += 2
        if self.Hhungry > 3000000000:
            self.state = "DEAD"
        else:
            pass
    def running(self):
        self.motion = "running"
        print(f"{self.nome} is running")
        
        while self.motion == "running":
            self.run()
            if self.state == "DEAD":
                return self.stop()
        else:
            return self.stop()
                
    def stop(self):
        self.motion = "stopped"
        print(f"{self.nome} is {self.motion}")
        return self.motion
    
    def check_for_stop_command(self, file_path):
        while self.motion == 'running':
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    command = file.read().strip()
                    if command == 'stop':
                        self.stop()
                        
            else:
                print("don't exist")
            sleep(1)

class Dog(Animals):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        

def main():
    before = datetime.now() 

    dog1 = Dog("scooby")
        #defining threads
    running_thread = Thread(target=dog1.running)
    command_task = Thread(target=dog1.check_for_stop_command, args=('command.txt',))
        # activate thread 1
    running_thread.start()
    
    print(dog1.Hhungry)
    sleep(2)
    print(dog1.Hhungry)
    
        # activate thread 2
    command_task.start()
        # merger parellel thread outcome
    command_task.join() 
        # merger parellel thread outcome
    running_thread.join()

    print(dog1.Hhungry)
    after = datetime.now()
    print(after-before)

if __name__ == "__main__":
    main()  

