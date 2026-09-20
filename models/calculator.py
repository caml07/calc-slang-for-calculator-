def calculate(expression):
    expression = expression.replace(" ", "")
    tokens = tokenize_expression(expression)

    try:
        result = solve_basic_expression(tokens)
    except ZeroDivisionError:
        return "Math Error"

    if result.is_integer():
        return int(result)

    return result


def tokenize_expression(expression):
    tokens = []
    number = ""

    for position, char in enumerate(expression):
        if char.isdigit() or char == ".":
            number += char
        elif char == "-" and (position == 0 or expression[position - 1] in "+-*/"):
            number += char
        else:
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)

    if number:
        tokens.append(float(number))

    return tokens


def solve_basic_expression(tokens):
    values = tokens.copy()

    index = 1
    while index < len(values):
        operator = values[index]

        if operator in ("*", "/"):
            left_number = values[index - 1]
            right_number = values[index + 1]

            if operator == "*":
                result = left_number * right_number
            else:
                result = left_number / right_number

            values[index - 1:index + 2] = [result]
            index = 1
        else:
            index += 2

    result = values[0]
    index = 1

    while index < len(values):
        operator = values[index]
        number = values[index + 1]

        if operator == "+":
            result += number
        else:
            result -= number

        index += 2

    return result
