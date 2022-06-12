"""The module provides a simple greeting function."""

from sympy import symbols


def greeting(name: str):
    """Print a simple greeting with the name."""
    print(f"Welcome {name} in Poland!")

def expresion(a, b):
    """Method only to check if library is properly installed"""
    x, y = symbols('x y')
    expr = x + 2*y
    value = expr.subs([(x, a), (y, b)])
    return value

