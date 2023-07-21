from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

mock_restrictions = {
    Restriction.ANIMAL_DERIVED,
    Restriction.ANIMAL_MEAT
    }


# Req 1
def test_ingredient():
    recipes = Ingredient("bacon")
    assert recipes.name == "bacon"
    assert recipes.__repr__() == "Ingredient('bacon')"
    assert recipes.restrictions == mock_restrictions
    assert len(f'{recipes.__hash__()}') == 20
    assert recipes.__eq__(recipes)
