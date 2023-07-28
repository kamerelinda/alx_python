def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers

    # Generate the Fibonacci numbers up to the nth number
    while len(fibonacci_numbers) < n:
        next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fibonacci)

    return fibonacci_numbers[:n]
