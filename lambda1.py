numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num,numbers)

print(list(squared_nums))  #[9, 49, 144, 324, 400, 441]

odd_nums= filter(lambda num: num%2 !=0, numbers)

print(list(odd_nums))   #[3, 7, 21]