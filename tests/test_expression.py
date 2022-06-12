from libproj.greeting import expresion


def test_expression():
    result = expresion(a=1, b=2)
    assert result == 5