def perform_operation(num1,num2,operation):
    if operation == "divide":
        return num1/num2
    elif operation == "multibly":
        return num1*num2
    elif operation == "add":
        return num1+num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is undefined."
        return num1 / num2
    else:
        return"Error: Invalid operation specified."
