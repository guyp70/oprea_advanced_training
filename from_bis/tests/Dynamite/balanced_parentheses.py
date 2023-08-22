PARENTHESES = {
    '(': ')',
    '{': '}',
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

    stack = []
    for parenthesis in expression:
        if parenthesis in PARENTHESES:
            stack.append(parenthesis)
        else:
            if not stack:
                return False
            popped_parenthesis = stack.pop()
            if popped_parenthesis in PARENTHESES and PARENTHESES[popped_parenthesis] != parenthesis:
                return False

    return not stack
