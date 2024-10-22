import doctest

def raw_credit(food_ate: float, multiplier: float) -> float:
    """
    Calculate raw credit based on food eaten and a multiplier.
    """
    assert type(food_ate) == float, "food_ate must be a float"
    raw_credit_value = food_ate * multiplier
    assert food_ate >= 0, 'food_ate must be non-negative'
    return max(raw_credit_value, 0)

def final_credit(raw_credit, opponent_raw_credit):
    """
    Calculate the final credit by subtracting 20% of the opponent's raw credit.
    The final credit cannot be negative.
    
    :param raw_credit: The raw credit of the current participant.
    :param opponent_raw_credit: The raw credit of the opponent.
    :return: The final credit (non-negative).
    """
    return max(raw_credit - 0.2 * opponent_raw_credit, 0)

def my_food_credit(my_food_ate: float, opp_food_ate: float) -> float:
    """
    Calculate my final food credit based on the food I ate and the food my opponent ate.
    
    :param my_food_ate: The amount of food I ate in kg.
    :param opp_food_ate: The amount of food my opponent ate in kg.
    :return: My final food credit in float.
    
    >>> my_food_credit(20.0, 10.0)
    170.0
    >>> my_food_credit(10.0, 20.0)
    40.0
    """
    assert type(opp_food_ate) == float, "opp_food_ate must be a float"
    assert type(my_food_ate) == float, "my_food_ate must be a float"
    assert my_food_ate >= 0, "my_food_ate must be non-negative"
    assert opp_food_ate >= 0, "opp_food_ate must be non-negative"

    my_raw = raw_credit(my_food_ate, 10)
    opp_raw = raw_credit(opp_food_ate, 15)
    return final_credit(my_raw, opp_raw)

def opponent_food_credit(opp_food_ate: float, my_food_ate: float) -> float:
    """
    Calculate my opponent's final food credit based on the food they ate and the food I ate.
    
    :param opp_food_ate: The amount of food my opponent ate in kg.
    :param my_food_ate: The amount of food I ate in kg.
    :return: My opponent's final food credit in float.
    
    >>> opponent_food_credit(10.0, 20.0)
    110.0
    >>> opponent_food_credit(20.0, 10.0)
    280.0
    """
    assert type(opp_food_ate) == float, "opp_food_ate must be a float"
    assert type(my_food_ate) == float, "my_food_ate must be a float"
    assert my_food_ate >= 0, "my_food_ate must be non-negative"
    assert opp_food_ate >= 0, "opp_food_ate must be non-negative"

    
    opp_raw = raw_credit(opp_food_ate, 15)
    my_raw = raw_credit(my_food_ate, 10)
    return final_credit(opp_raw, my_raw)

if __name__ == "__main__":
    doctest.testmod()