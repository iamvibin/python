#this is the template for making the PARTY ANIMAL OBJECTS
class PartyAnimal:
    x=0
    name = ""
    def __init__(self,z):
        self.name = z
        print('I am constructed', self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name,"AS OF NOW",self.x)

    def __del__(self):
        print('I am destructed at the value of ',self.x)

# footballfan is a class which extends PartyAnimal. I t has all the capabilities of PartyAnimal and more
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)
an = PartyAnimal("Sally")#CREATES AN INSTANCE USING THE TEMPLATE GIVEN IN CLASS (PARTY ANIMAL)
an.party()

print("TYPE", type(an))#getys the type  as the name suggests
print("Dir", dir(an))# gets the method and attributes of thge class

j = PartyAnimal("Jim")
j.party()
print("an contains",an)
an = 42 #destructor is called and an assigned with integer of val 2
print("an contains",an)
k = FootballFan("tim")
k.party()
k.touchdown()
