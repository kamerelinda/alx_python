def is_prime(number):

    if number < 2:
        return False
    else:
        # Check for factors from 2 up to the square root of the number
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
