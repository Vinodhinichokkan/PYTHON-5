#lambda

squared = lambda num : num * num
print(squared(3))    #9

add_two = lambda num : num + 2

print (add_two(8))   #10

#incase of function we write it as

#def add_two(num): return num + 2

sum_total = lambda a, b : a + b

print(sum_total(5,5))   #10

#def sum_total(a,b): return a + b

def funcBuilder(x):
    return lambda num: num + x

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))   #17
print(add_twenty(7))   #27



