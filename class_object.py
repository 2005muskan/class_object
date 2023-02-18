class watch():
    
    def __init__(self,name,surname,cla,college):
        print("Hello student")
        self.name = name
        self.surname = surname
        self.cla = cla
        self.college= college   
    def fight(self):
        print("How are you all")
        print("your name is:",self.name,"\n")
        print("your surname is:",self.surname,"\n")
        print("your class is :",self.cla,"\n")
        print("your college is :",self.college,"\n")
        
obj = watch("muskan","kushwah","second year","madhav science college")

obj.fight()
