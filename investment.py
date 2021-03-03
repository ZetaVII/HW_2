def calculate_apr(principal, interest_rate, years):
    """
    Calculates the user's total investment based on their arguments.

    Parameters
    ----------
    principal : float
        Inital amount the user starts off with.

    interest_rate : float
        The annual interest that gets added to 
        the user's total investment

    years: int
        Total investment years

    Returns
    -------
    float
        Returns the total investment accumulated over
        years based on their initial value and interest
        rate

    Examples
    --------
    >>> calculate_apr(500, 0.03, 5)
    579.6370371500001

    >>> calculate_apr(500, 0.03, 65)
    3414.9913672928196

    >>> calculate_apr(1000, 0.05, 65)
    23839.90055917926
    """
    if(interest_rate < 0):
        return False
    
    # General equation used to calculate total investments
    temp = principal * (1 + interest_rate)**years

    return temp

