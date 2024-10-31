def get_store1_revenue(store1_monthly_sales: float) -> float:
    """
    Calculates the revenue for store 1 based on its monthly sales.
    
    :param store1_monthly_sales: Monthly sales of store 1
    :return: Revenue of store 1
    """
    return store1_monthly_sales / 5

def get_store2_revenue(store2_monthly_sales: float) -> float:
    """
    Calculates the revenue for store 2 based on its monthly sales.
    
    :param store2_monthly_sales: Monthly sales of store 2
    :return: Revenue of store 2
    """
    return store2_monthly_sales / 8

def get_total_revenue(store1_monthly_sales: float, store2_monthly_sales: float) -> float:
    """
    Calculates total revenue based on store 1 and store 2 monthly sales.

    >>> get_total_revenue(800.0, 600.0)
    235.0
    >>> get_total_revenue(1000.0, 800.0)
    300.0
    >>> get_total_revenue(0.0, 0.0)
    0.0
    >>> get_total_revenue(500.0, 1600.0)
    300.0

    :param store1_monthly_sales: Monthly sales of store 1
    :param store2_monthly_sales: Monthly sales of store 2
    :return: Total revenue of both stores
    """
    assert type(store1_monthly_sales) == float, 'invalid argument'
    assert store1_monthly_sales >= 0, 'must be non-negative'
    assert type(store2_monthly_sales) == float, 'invalid argument'
    assert store2_monthly_sales >= 0, 'must be non-negative'

    store1_revenue = get_store1_revenue(store1_monthly_sales)
    store2_revenue = get_store2_revenue(store2_monthly_sales)

    total_revenue = store1_revenue + store2_revenue

    return total_revenue

if __name__ == "__main__":
    import doctest
    doctest.testmod()
