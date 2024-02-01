class Notebook:
    def __init__(self):
        self._ram = []
        self._screen_size = []

    def insert_screens(self, *screens):
        self._screen_size.extend(screens)

    def list_screens(self):
        print()
        print('screen options:')
        for screen in self._screen_size:
            print(screen)
    
    def insert_ram(self, *memories):
        #self._ram += memory
        #self._ram.extend(memory)
        for memory in memories:
            self._ram.append(memory)

    def list_ram(self):
        print()
        print('memory options:')
        for ram in self._ram:
            print(ram)
    
class Screen:
    def __init__(self, size):
        self.size = size
    
    def __str__(self):
        return f"Screen Size: {self.size}"
class Ram:
    def __init__(self, memory):
        self.memory = memory

    def __str__(self):
        return f"memory: {self.memory}"


# class to set laptop configuration
class Notebook_choice():
    def __init__(self, notebooks):
        self.notebooks = notebooks
        self.choice = []
    
    
    #choosing instance's screen
    def screen_choice(self):
        
        print("which screen do you want:")
        for i,screen in enumerate(self.notebooks._screen_size):
            print()
            print(f"{i}. {screen}")
        screen = int(input("choice: "))
        
        self.choice.append(str(self.notebooks._screen_size[screen]))
    def ram_choice(self):
        
        print("which memory do you want:")
        for i,ram in enumerate(self.notebooks._ram):
            print()
            print(f"{i}. {ram}")
        ram =  int(input("choice: "))
        
        self.choice.append(str(self.notebooks._ram[ram]))
    def show_product(self):
        print(f"your product has the following specs ->", {*self.choice})


# creating notebook instances
inspiron = Notebook()
g15 = Notebook()
vevo = Notebook()
xps = Notebook()

# creating screen instances 
screen1,screen2,screen3,screen4 = Screen('15'), Screen('16'), Screen('17'), Screen('14')

#creating memory instances
memory1,memory2,memory3,memory4,memory5 = Ram('4'),Ram('8'),Ram('16'),Ram('32'),Ram('64')

# inserting scren size and memory length in list of options
inspiron.insert_screens(screen1,screen2)
inspiron.insert_ram(memory1,memory2,memory3)

g15.insert_ram(memory1,memory2,memory3,memory4)
g15.insert_screens(screen1)

vevo.insert_screens(screen4)
vevo.insert_ram(memory4,memory3, memory5)

xps.insert_ram(memory2, memory4,memory3, memory5)
xps.insert_screens(screen4)

inspiron.list_screens()
inspiron.list_ram()


# defining laptop configuration
choice1 = Notebook_choice(inspiron)
choice1.screen_choice()
choice1.ram_choice()
choice1.show_product()

# defining laptop configuration
choice2 = Notebook_choice(xps)
choice2.screen_choice()
choice2.ram_choice()
choice2.show_product()