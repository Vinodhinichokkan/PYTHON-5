#f-strings---------->formatted strings

person ="Vinodhini"
coins =3

#--------------------
#Concatenating strings

print("\n" +  person +  " has " +  str(coins)  + " Coins left. ")

                                #Vinodhini has 3 Coins left.
#-----------------------
#previous %s formatting

message = "\n%s has %s coins left." % (person,coins)
print (message)
                          #Vinodhini has 3 Coins left.
#------------------------
#previous string.format() method

message = "\n{} has {} coins left." .format(person, coins)
print(message)            #Vinodhini has 3 Coins left.

message = "\n{1} has {0} coins left." .format(coins, person)
print(message)            #Vinodhini has 3 Coins left

message = "\n{person} has {coins} coins left." .format(coins=coins, person=person)
print(message)             #Vinodhini has 3 Coins left


print('')

player ={'person': 'Abi', 'coins': 3}
message ="\n {person} has {coins} coins left." .format(**player)
print(message)    #Abi has 3 coins left.

