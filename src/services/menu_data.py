from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    __recipes: list[str] = []
    dishes: set[Dish] = set()

    def __init__(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            self.menu = file.readlines()
        for row in self.menu[1:]:
            name, price = row.split(",")[:2]
            item_recipes = ", ".join([name, price])
            if item_recipes not in self.__recipes:
                self.__recipes.append(item_recipes)
        self.init_dish()

    def init_dish(self):
        for recipe in self.__recipes:
            name_recipes, price_recipes = recipe.split(',')
            menu = Dish(name=name_recipes, price=float(price_recipes))
            for row in self.menu:
                name, price, item, amount = row.replace('\n', '').split(",")
                if name_recipes == name:
                    menu.add_ingredient_dependency(
                        ingredient=Ingredient(item),
                        amount=int(amount)
                        )
            self.dishes.add(menu)
