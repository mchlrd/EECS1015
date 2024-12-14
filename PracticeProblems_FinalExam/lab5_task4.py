import doctest


def calculate_raw_credit(food_ate: float, multiplier: float) -> float:
    """
    Helper function to calculate raw credit based on food eaten and multiplier.

    Args:
        food_ate (float): The amount of food eaten.
        multiplier (float): The multiplier for the class (10 for Flyweight, 15 for Strawweight).

    Returns:
        float: The raw credit.
    """
    return food_ate * multiplier


def calculate_final_credit(raw_credit: float, opp_raw_credit: float) -> float:
    """
    Helper function to calculate the final credit after deducting 20% of opponent's raw credit.

    Args:
        raw_credit (float): The raw credit of the participant.
        opp_raw_credit (float): The raw credit of the opponent.

    Returns:
        float: The final credit (non-negative).
    """
    return max(raw_credit - 0.2 * opp_raw_credit, 0)


def my_food_credit(food_ate: float, opp_food_ate: float) -> float:
    """
    Calculate the final credit for the Flyweight participant (you).

    Args:
        food_ate (float): The amount of food you ate.
        opp_food_ate (float): The amount of food your opponent ate.

    Returns:
        float: The final credit for you.
    """
    assert isinstance(food_ate, float), "invalid argument type"
    assert isinstance(opp_food_ate, float), "invalid argument type"
    assert food_ate >= 0, 'invalid argument value'
    assert opp_food_ate >= 0, 'invalid argument value'

    my_raw_credit = calculate_raw_credit(food_ate, 10)
    opp_raw_credit = calculate_raw_credit(opp_food_ate, 15)

    return calculate_final_credit(my_raw_credit, opp_raw_credit)


def opponent_food_credit(opp_food_ate: float, food_ate: float) -> float:
    """
    Calculate the final credit for the Strawweight participant (opponent).

    Args:
        opp_food_ate (float): The amount of food your opponent ate.
        food_ate (float): The amount of food you ate.

    Returns:
        float: The final credit for your opponent.
    """
    assert isinstance(food_ate, float), "invalid argument type"
    assert isinstance(opp_food_ate, float), "invalid argument type"
    assert food_ate >= 0, 'invalid argument value'
    assert opp_food_ate >= 0, 'invalid argument value'

    opp_raw_credit = calculate_raw_credit(opp_food_ate, 15)
    my_raw_credit = calculate_raw_credit(food_ate, 10)

    return calculate_final_credit(opp_raw_credit, my_raw_credit)


if __name__ == "__main__":
    doctest.testmod()