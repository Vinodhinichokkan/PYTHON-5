name = "Vinodhini" #----------->Global scope

def greeting(name): #----------->Local scope
    age = 30          
    print(age)      #30
    print(name)    #Subscribe

greeting("Subscribe")   
print(name)     #Vinodhini


print('')
name = "Vinodhini"

def greeting(name):
    age = 30
    print(age)    #30
    print(name)   #Subscribe
    print(name)   #Subscribe

greeting("Subscribe")


print('')

name = "Vinodhini"

def another():
    def greeting(name):
        age = 30
        print(age)    #30
        print(name)   #Share 
          

    greeting("Share")

another()

