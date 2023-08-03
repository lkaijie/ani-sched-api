

class Sample:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def hello(self):
        print("Hello, "+self.name)