class Animal:

    def __init__(self, color, claws) :
        self._animal_color = color
        self._has_claws = claws

    def color_getter(self):
        return self.color
    
    @property
    def color(self):
        print("PROPERTY: cor")
        return self._animal_color
    
    @color.setter
    def color(self,value):
        print("I'm in the setter!")
        if value != "black" or value != "grey":
            raise ValueError(f"no ravenclaw has the color {value}.")
        self._animal_color = value

    @property
    def claws(self):
        return self._has_claws
    @claws.setter    
    def claws(self,value):
        self._has_claws = value


    


ravenclaw = Animal("black", 'no')


print(ravenclaw.color_getter())

print(ravenclaw.color)

#ravenclaw.color = "pink"

print(ravenclaw.color)

ravenclaw.claws ="yes"

print(ravenclaw.claws)