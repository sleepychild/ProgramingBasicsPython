from typing import List


class Catalogue:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.products: List[str] = list()

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> List[str]:
        return list(filter(lambda p: p.startswith(first_letter.upper()) or p.startswith(first_letter.lower()), self.products))

    def __repr__(self) -> str:
        rtrn_str: str = str()
        rtrn_str += f'Items in the {self.name} catalogue:\n'
        pl: List[str] = sorted(self.products)
        rtrn_str += '\n'.join(pl)
        return rtrn_str

# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)

# catalogue = Catalogue("")
# catalogue.add_product("desk")
# catalogue.add_product("chair")
# catalogue.add_product("")
# catalogue.add_product("")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# catalogue.add_product("12asd")
# catalogue.add_product("13asd")
# print(catalogue.get_by_letter("C"))
# print(catalogue.get_by_letter("D"))
# print(catalogue.get_by_letter("A"))
# print(catalogue)
