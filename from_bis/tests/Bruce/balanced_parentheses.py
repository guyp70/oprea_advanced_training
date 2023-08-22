ALL_PARENTHESES = '()', '[]', '{}'


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

    while any(parenthesis in expression for parenthesis in ALL_PARENTHESES):
        for parenthesis in ALL_PARENTHESES:
            if parenthesis in expression:
                expression = expression.replace(parenthesis, '')
    return bool(expression)
