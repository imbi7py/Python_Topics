from Previous.sandwich ______ sandwich

SANDWICH_BACON = """=== Upper bread slice ===
bacon / lettuce / tomato
=== Lower bread slice ===
"""
SANDWICH_EGG = """=== Upper bread slice ===
fried egg / tomato / cucumber
=== Lower bread slice ===
"""


@sandwich
___ add_ingredients(ingredients
    print(' / '.join(ingredients))


___ test_bacon_sandwich(capfd
    ingredients = ['bacon', 'lettuce', 'tomato']
    add_ingredients(ingredients)
    actual = capfd.readouterr()[0]
    assert actual __ SANDWICH_BACON


___ test_fried_egg_sandwich(capfd
    ingredients = ['fried egg', 'tomato', 'cucumber']
    add_ingredients(ingredients)
    actual = capfd.readouterr()[0]
    assert actual __ SANDWICH_EGG