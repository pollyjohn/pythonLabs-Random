class Writer:
    def __init__(self,name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool

class WrittingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f"{self.name} is writing"

writer = Writer('Apolo')
pen = WrittingTool('Bic pen')
writing_machine = WrittingTool('machine')
writer.tool = writing_machine

# as it is a week association we can use tools non attached to a writter
print(pen.write())
print(writing_machine.write())
print(writer.tool.write())
