def calculate_apr(principal, interest_rate, years):

    if(interest_rate < 0):
        return False
    
    temp = principal * (1 + interest_rate)**years

    return temp

