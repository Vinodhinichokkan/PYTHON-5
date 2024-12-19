# ----------classes--------

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')  #Moves along..

    def get_make_model(self):     #I'm a Tesla Model Y.
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla','Model Y')

my_car.moves()
print(my_car.make)   #Tesla
print(my_car.model)  #Model Y
my_car.get_make_model() 

print('')

#--------------------Inheritance-------------------

class Airplane(Vehicle):
    def moves(self):
        print('Rumbles along..')
      
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna','Skywalk')
mack = Truck('Mack','Pinnacle')
golfwagon = GolfCart('Yamaha','GC100')

cessna.get_make_model()       #I'm a Cessna Skywalk.
                              #Rumbles along..
                              #I'm a Mack Pinnacle.
                              #Rumbles along..
                              #I'm a Yamaha GC100.
                              #Moves along..
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print('')

for v in(my_car, cessna, mack,golfwagon):
    v.get_make_model()
    v.moves()

#I'm a Tesla Model Y.
#Moves along..
#I'm a Cessna Skywalk.
#Rumbles along..
#I'm a Mack Pinnacle.
#Rumbles along..
#I'm a Yamaha GC100.
#Moves along..


    
