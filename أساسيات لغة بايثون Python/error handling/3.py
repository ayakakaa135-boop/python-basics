"""try:
    x=6
    y=3
    print(x%(x-y))

except:
    print('Did you divide by zero')
    """

try:
    with open('file.txt', 'a') as file:
        x = 6
        y = 3
        result = (x + y) % (x - y)
        file.write(f'\nThe result is {result}')

except FileNotFoundError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print('The result was written to the file')
finally:
    print('Code execution was finished')
