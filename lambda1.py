numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num,numbers)#-------------->map will match the each and every element in the list

print(list(squared_nums))  #[9, 49, 144, 324, 400, 441]

odd_nums= filter(lambda num: num%2 !=0, numbers)#------------>filter will check whether the given condition is true or false.

print(list(odd_nums))   #[3, 7, 21]

from functools import reduce
numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc  + curr ,numbers)
print (total)    #16

#---------another method
print(sum(numbers))  #16


names = ['Vinodhini','Abirami','Hari']
char_count = reduce(lambda acc,curr: acc + len(curr), names, 0)#---->0 is to convert string to number
print(char_count)  #20

