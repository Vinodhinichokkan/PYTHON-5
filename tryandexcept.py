x = 2
try:
    print(x/0)
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError as error:
    print('Please donot divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")
    