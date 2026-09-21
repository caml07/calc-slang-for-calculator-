import math


def calculate(expression):
    expression = expression.replace(" ", "")

    try:
        if not expression or not has_valid_parentheses(expression) or "%%" in expression:
            return "Syntax Error"

        tokens = tokenize_expression(expression)
        result = solve_parentheses(tokens)
    except (ZeroDivisionError, OverflowError):
        return "Math Error"
    except (IndexError, TypeError, ValueError):
        return "Syntax Error"

    if not math.isfinite(result):
        return "Math Error"

    if result.is_integer():
        return int(result)

    return result


def has_valid_parentheses(expression):
    open_parentheses = 0

    for char in expression:
        if char == "(":
            open_parentheses += 1
        elif char == ")":
            open_parentheses -= 1
            if open_parentheses < 0:
                return False

    return open_parentheses == 0


def solve_parentheses(tokens):
    values = tokens.copy()

    while "(" in values:
        open_position = len(values) - 1 - values[::-1].index("(")
        close_position = values.index(")", open_position)

        inside = values[open_position + 1:close_position]
        result = solve_basic_expression(inside)

        if open_position > 0 and values[open_position - 1] in ("sqrt", "sin", "cos", "tan", "log", "ln"):
            function = values[open_position - 1]

            if function == "sqrt":
                if result < 0:
                    raise ZeroDivisionError
                result = math.sqrt(result)
            elif function == "sin":
                result = math.sin(math.radians(result))
            elif function == "cos":
                result = math.cos(math.radians(result))
            elif function == "tan":
                result = math.tan(math.radians(result))
            elif function == "log":
                if result <= 0:
                    raise ZeroDivisionError
                result = math.log10(result)
            else:
                if result <= 0:
                    raise ZeroDivisionError
                result = math.log(result)

            values[open_position - 1:close_position + 1] = [result]
        else:
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

        if expression[position:position + 4] == "sqrt":
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append("sqrt")
            position += 4
            continue

        function = expression[position:position + 3]
        if function in ("sin", "cos", "tan", "log"):
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(function)
            position += 3
            continue

        if expression[position:position + 2] == "ln":
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append("ln")
            position += 2
            continue

        if char.isdigit() or char == ".":
            number += char
        elif char == "-" and (position == 0 or expression[position - 1] in "+-*/^("):
            number += char
        else:
            if char not in "+-*/^%()":
                raise TypeError
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
