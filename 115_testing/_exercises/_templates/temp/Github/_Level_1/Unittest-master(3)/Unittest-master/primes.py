___ is_prime(number):
    """Return True if *number* is prime."""
    if number <_ 1:
        r_ False


    for element in range(2,number):
        if number % element == 0:
            r_ False

    r_ True

___ print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index _ number
    while True:
        index +_ 1
        if is_prime(index):
            print(index)
