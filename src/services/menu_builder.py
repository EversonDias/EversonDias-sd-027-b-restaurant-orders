from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        result: list = list()
        inventory = set(self.inventory.inventory)
        for dishes in self.menu_data.dishes:
            dishes_restriction = dishes.get_restrictions()
            dishes_ingredients = dishes.get_ingredients()
            isAvailable = dishes_ingredients.issubset(inventory)
            if restriction not in list(dishes_restriction) and isAvailable:
                new_dishes = {
                        "dish_name": dishes.name,
                        "ingredients": dishes_ingredients,
                        "price": dishes.price,
                        "restrictions": dishes_restriction,
                    }
                result.append(new_dishes)
        return result
