class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    @property
    def area(self):
        return self.width*self.height


r=Rectangle(5,6)
print(r.area)