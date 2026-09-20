import math


def calculate(expression):
    expression = expression.replace(" ", "")
    tokens = tokenize_expression(expression)

    try:
        result = solve_parentheses(tokens)
    except ZeroDivisionError:
        return "Math Error"

    if result.is_integer():
        return int(result)

    return result


def solve_parentheses(tokens):
    values = tokens.copy()

    while "(" in values:
        open_position = len(values) - 1 - values[::-1].index("(")
        close_position = values.index(")", open_position)

        inside = values[open_position + 1:close_position]
        result = solve_basic_expression(inside)
        values[open_position:close_position + 1] = [result]

    return solve_basic_expression(values)


def tokenize_expression(expression):
    tokens = []
    number = ""
    position = 0

    while position < len(expression):
        char = expression[position]

        if expression[position:position + 2] == "pi":
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(math.pi)
            position += 2
            continue

        if char.isdigit() or char == ".":
            number += char
        elif char == "-" and (position == 0 or expression[position - 1] in "+-*/"):
            number += char
        else:
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)

        position += 1

    if number:
        tokens.append(float(number))

    return tokens


def solve_basic_expression(tokens):
    values = tokens.copy()

    while "%" in values:
        percent_position = values.index("%")
        number = values[percent_position - 1]
        values[percent_position - 1:percent_position + 1] = [number / 100]

    while "^" in values:
        operator_position = len(values) - 1 - values[::-1].index("^")
        left_number = values[operator_position - 1]
        right_number = values[operator_position + 1]
        result = left_number ** right_number
        values[operator_position - 1:operator_position + 2] = [result]

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
