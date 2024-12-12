def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


#multiplier of 3

times3 = make_multiplier_of(3)

#multiplier of 4

times5 = make_multiplier_of(5)

print(times3(9))  #27

print(times5(3))  #15