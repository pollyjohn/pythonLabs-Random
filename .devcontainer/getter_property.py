class Animal:

    def __init__(self, color, claws= True) :
        self.animal_color = color
        self.has_claws = claws

    def color_getter(self):
        return self.color
    
    @property
    def color(self):
        print("PROPERTY: cor")
        return self.animal_color
    
    @property
    def claws(self):
        if self.has_claws:
            return "yes"
        else:
            return "no"


ravenclaw = Animal("black", False)


print(ravenclaw.color_getter())

print(ravenclaw.color)

print(ravenclaw.claws)




