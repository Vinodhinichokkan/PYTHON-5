name="Vinodhini"
age =25
def another():
    global age#------------if we need to use global variable in local scope use global keyword
    age += 2
    color = 'green'
    def greeting(name):
        print(age)      #27
        nonlocal color
        color = 'red'
        print(color)   #red
        print(name)   #Share
    greeting("Share")

another()


