def gcd_euclid(a, b):
    """
    Calculates the Greatest Common Denominator (GCD) using Euclid's algorithm.
    
    The Euclid's algorithm is based on the principle that the GCD of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.
    
    Reference: https://www.w3schools.com/dsa/dsa_ref_euclidean_algorithm.php

    The while loop will continue until 'b' is equal to 0.
    In each iteration, 'a' is replaced with 'b' and 'b' is replaced with the remainder of 'a' divided by 'b'.
    The loop will continue until 'b' is equal to 0, at which point the value of 'a' will be the GCD of the two numbers.
    """
    while b != 0:
        a, b = b, a % b  # Replace a with b and b with the remainder of a divided by b
    return a
