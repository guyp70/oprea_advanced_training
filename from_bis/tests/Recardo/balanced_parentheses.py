PARENTHESES = {
    '(': ')',
    '[': ']',
}


def parentheses_are_balanced(expression: str) -> bool:
    """
    Check if the given string has balanced parentheses, meaning:
    1. Open parentheses must be closed by the same type of parentheses.
    2. Open parentheses must be closed in the correct order.
    3. Every closing parenthesis has a corresponding open parenthesis of the same type.

    :param expression: The string to check for balanced parentheses.
    :return: True if the parentheses are balanced, False otherwise.
    """
    if not isinstance(expression, str):
        raise TypeError(f'Expected str, got {type(expression)}')

    length = len(expression)
    if length == 0:
        return True
    if length == 1:
        return False
    if expression[0] not in PARENTHESES:
        return False

    opening_parenthesis = expression[0]
    closing_parenthesis = PARENTHESES[opening_parenthesis]
    open_count = 0
    closed_count = 0
    i = -1
    for i in range(0, length):
        if expression[i] == opening_parenthesis:
            open_count += 1
        elif expression[i] == closing_parenthesis:
            closed_count += 1
        if open_count == closed_count:
            break

    if closed_count < open_count:
        return False

    if i == 1:
        return parentheses_are_balanced(expression[2:])

    return (
        parentheses_are_balanced(expression[1:i]) and
        parentheses_are_balanced(expression[i + 1:])
    )
