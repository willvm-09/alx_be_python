def perform_operations(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num1 and num2 !== 0:
            result = num1 / num2
return result
perform_operations()
