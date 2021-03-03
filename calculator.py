def input_output():
    """
    Request user inputs for the two numbers and 
    operator in a continuous loop until the user
    ends with a "Y" || "y" or when an invalid
    argument has been inputted

    Returns
    -------
    Float
        Results contains the outcome of the two
        numbers based on the chosen operator

    Examples
    --------
    Enter the first number: 10
    Enter the second number: 2
    Enter the operation: +
    12.0

    Do you wish to exit (Y/N):  n
    Enter the first number: 12
    Enter the second number: 4.2
    Enter the operation: *
    50.400000000000006

    Do you wish to exit (Y/N):  n
    Enter the first number: 10
    Enter the second number: 2
    Enter the operation: **
    100.0

    Do you wish to exit (Y/N):  y
    >>>
    """
    y = True
    
    while y:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        operator = input("Enter the operation: ")

        number1 = float(number1)
        number2 = float(number2)

        results = calculator(number1, number2, operator)
        
        # Program will terminate if an invalid argument has 
        # been inputted into one of the parameters.
 
        if( not results):
            break;

        # User determines to continue with program 
        y = input("Do you wish to exit (Y/N): ")
        
        if(y == "n" or y == "N"):
            continue
        else:
            break

def calculator(number1, number2, operator):
    """
    This function is called to perform arithmitic calculations
    based on the passed parameters from any calling function

    Parameters
    ----------
    number1 : float
        First value on the left side of the operator

    number2 : float
        Second value on the right side of the operator
    
    operator: string
        Determines which of the preset operators to 
        perform the calculations. 

    Returns
    -------
    float
        Returns the valid outcome of the calculations

    Examples
    --------
    calculator(3.0, 6.0, "+")
    9.0

    calculator(3.0, 3.0, "**")
    27.0
    """

    # Initializes the total value to store 
    # the outcome of the calculations
    total = 0.0

    if operator == "+":
        total = number1 + number2
    elif operator == "-":
        total = number1 - number2
    elif operator == "*":
        total = number1 * number2
    elif operator == "/":
        total = number1 / number2
    elif operator == "//":
        total = number1 // number2
    elif operator == "**":
        total =  number1 ** number2
    
    # If an invalid operator has been inserted,
    # this function will return false to terminate
    # input_output()
    else:
        return False
    
    return total

# Sets the input_output() as default
# when running this Python file

if __name__ == '__main__':
    input_output()
    