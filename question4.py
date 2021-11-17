class Question4:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
    def areacalc(self):
        radius=12
        area=(radius*3.142)
        print("area is: ",area)
    def perimetercalc(self):
        radius=1
        perimeter=(2*3.142)*radius
        print("Perimeter is: ",perimeter)
Object=Question4('Steve','Gant')
Object.areacalc()
Object.perimetercalc()
