import doctest

def get_total_revenue(store1_monthly_sales: float, store2_monthly_sales: float) -> float:
    '''


    Args:
        store1_monthly_sales:
        store2_monthly_sales:

    Returns:

    >>> get_total_revenue(800.0, 600.0)
    235.0
    >>> get_total_revenue(1000.0, 800.0)
    300.0
    >>> get_total_revenue(0.0, 0.0)
    0.0
    >>> get_total_revenue(500.0, 1600.0)
    300.0
    '''
    assert type(store1_monthly_sales) == float, 'invalid argument type'
    assert type(store2_monthly_sales) == float, 'invalid argument type'

    store1_monthly_sales = get_store1_revenue(store1_monthly_sales)
    store2_monthly_sales = get_store2_revenue(store2_monthly_sales)

    return store1_monthly_sales + store2_monthly_sales

def get_store1_revenue(store1_monthly_sales: float) -> float:
    assert type(store1_monthly_sales) == float, 'invalid argument type'
    assert store1_monthly_sales >= 0, 'revenue must be non-negative'

    return store1_monthly_sales / 5

def get_store2_revenue(store2_monthly_sales: float) -> float:
    assert type(store2_monthly_sales) == float, 'invalid argument type'
    assert store2_monthly_sales >= 0, 'revenue must be non-negative'

    return store2_monthly_sales / 8

if __name__ == "__main__":
    doctest.testmod()
