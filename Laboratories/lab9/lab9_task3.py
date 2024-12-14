from typing import Dict
def add_to_inventory(inventory: Dict[str, int], product: str, quality: int) -> int:
        '''

        Args:
            inventory: dictionary with keys and values
            product: string that contains a product
            quality: quantity of the product (int)

        Returns: int: number the product has been evaluated to

        >>> add_to_inventory({"Laptop": 21, "Smartphone": 15, "Tablet": 30, "Headphones": 11}, "Pineapple", 1)
        1
        >>> add_to_inventory({"Laptop": 21, "Smartphone": 15, "Tablet": 30, "Headphones": 11}, "Headphones", 2)
        13
        >>> add_to_inventory({"Laptop": 21, "Smartphone": 15, "Tablet": 30, "Headphones": 11}, "Tablet", 10)
        40
        >>> add_to_inventory({"Laptop": 21, "Smartphone": 15, "Tablet": 30, "Headphones": 11}, "Smartphone", 20)
        35
        '''

        assert type(inventory) == dict, 'invalid input type'
        assert type(product) == str, 'invalid input type'
        assert type(quality) == int and quality >= 0, 'quality must be a non-negative integer'

        if product in inventory:
            inventory[product] += quality
        else:
            inventory[product] = quality


        return inventory[product]

