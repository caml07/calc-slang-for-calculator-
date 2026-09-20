def calculate(expression):
    numbers = expression.split("+")

    left_number = float(numbers[0].strip())
    right_number = float(numbers[1].strip())

    result = left_number + right_number

    if result.is_integer():
        return int(result)

    return result
