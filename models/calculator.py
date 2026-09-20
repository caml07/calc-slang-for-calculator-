def calculate(expression):
    expression = expression.strip()

    if "+" in expression:
        numbers = expression.split("+")
        left_number = float(numbers[0].strip())
        right_number = float(numbers[1].strip())
        result = left_number + right_number
    else:
        minus_position = expression.find("-", 1)
        left_number = float(expression[:minus_position].strip())
        right_number = float(expression[minus_position + 1:].strip())
        result = left_number - right_number

    if result.is_integer():
        return int(result)

    return result
