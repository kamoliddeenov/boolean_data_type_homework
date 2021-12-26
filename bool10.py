def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    ildiz = a**0.5 
    return int(ildiz + 0.5) ** 2 == a

print(main(16))