import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

mock_restrictions = {
    Restriction.ANIMAL_DERIVED,
    Restriction.ANIMAL_MEAT
    }


# Req 2
def test_dish():
    item_menu_1 = Dish("feijoada", 45.50)
    item_menu_2 = Dish("PF", 14.99)
    item_menu_1.add_ingredient_dependency(
            ingredient=Ingredient("bacon"),
            amount=100
        )
    assert item_menu_1.name == "feijoada"
    assert hash(item_menu_1) != hash(item_menu_2)
    assert hash(item_menu_1) == hash(item_menu_1)
    assert item_menu_1.__eq__(item_menu_1)
    assert repr(item_menu_1) == "Dish('feijoada', R$45.50)"
    assert len(item_menu_1.get_ingredients()) == 1
    assert item_menu_1.get_restrictions() == mock_restrictions
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Nome do Prato", "20.00")
    messageError = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=messageError):
        Dish("Arroz doce", -10)
