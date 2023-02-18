class name:

    My = " Hello Everyone"
    print("sum number is : ")

    def __init__(self,M,N):
        self.M = M
        self.N = N

        print(self.M,)
        print(self.N)

    @classmethod
    def selary(cls,number):
        print("selary is : ")
        cls.number = number
        print(cls.number)


    def Num1(self, name1,name2,name3):
        self.X = name1
        self.Y = name2
        self.Z = name3

        print(self.X) 
        print(self.Y)
        print(self.Z)   

    def Num2(self,surname1,surname2,surname3):
        self.A = surname1
        self.B = surname2
        self.C = surname3

        print(self.A)
        print(self.B)
        print(self.C)


    def Num3(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

        print(self.x)
        print(self.y)
        print(self.z)

obj = name(25+27,34+56)
print(obj.My)
print("++++++++++++++++++++++")
obj.Num1("Muskan","Antim","Mahika")
print("++++++++++++++++++++++")
obj.Num2("Kushwah","manglani","Kushwah")
print("++++++++++++++++++++++++")
obj.Num3("Hii","How are you","I am fine")
obj.selary(100)




