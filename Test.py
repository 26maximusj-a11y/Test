class Fruit:
    def __init__(self,color,shape,taste,name):
        self.color = color
        self.shape = shape
        self.taste = taste
        self.name = name

    def get_shape(self):
        return self.shape

    def get_name(self):
        return self.name

fruity = Fruit("Red","round","Fruity","Apple")
shapes = fruity.get_shape()
print (shapes)