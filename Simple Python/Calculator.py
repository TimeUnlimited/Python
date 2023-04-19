print('Welcome to the calculator!')

# Here is where the variables are entered
num1 = float(input('Please enter the first number: '))
option = input('Please insert the symbol you would like to use EX: +-/* : ')
num2 = float(input('Please enter the last number: '))

# Here is the code that performs the arithmetic operation based on the user input symbol
if option == '+':
    result = num1 + num2
elif option == '-':
    result = num1 - num2
elif option == '*':
    result = num1 * num2
elif option == '/':
    result = num1 / num2
else:
    print('Invalid operator')

# Here is the code that displays the result
print('The answer is: ' + str(result))
