class square:
    var1=int(input("Enter a Number: "))

    def Calsarea(self):
        area=self.var1*self.var1
        print(area)

    def Calperimeter(self):
        perimeter=4*self.var1
        print(perimeter)

c=square()
x=c.Calsarea()
x=c.Calperimeter()
