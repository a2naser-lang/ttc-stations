
# needs some functions to do work here
# need something to determine MP eligibality 
# need something to determine Senator 

def mp_eligibility(is_citizen, age):
    """TODO: Write a good doc string."""
    min_age = 18
    result = is_citizen and age >= min_age
    return result

def senator_eligibility(is_citizen, age, net_worth):
    """TODO write docstring"""
    return None



def main():
    is_citizen = True # True if canadaian citizen, o.w. False.
    age = 55          # age in years
    net_worth = 5000  # net worth in dollars

    can_be_mp = None
    can_be_senator = None
    print("Eligable to be and MP?", can_be_mp)
    print("Eligable to be a Senator?", can_be_senator)

if __name__ == "__main__":
    main()