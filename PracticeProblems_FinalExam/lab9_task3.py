from typing import Dict

def add_to_inventory(inventory: Dict[str, int], product: str, quantity: int) -> int:
    '''

    Args:
        inventory:
        product:
        quantity:

    Returns:

    '''

    assert type(inventory) == dict, 'invalid argument type'
    assert type(product) == str, 'invalid argument type'
    assert type(quantity) == int, 'invalid argument type'

    assert quantity >= 0, 'invalid argument position'

    if product in inventory:

        inventory[product] += quantity

    else:

        inventory[product] = quantity

    return inventory[product]