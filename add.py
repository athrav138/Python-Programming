def add(a, b):
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    import sys
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input: please enter numeric values.")
        sys.exit(1)

    result = add(a, b)
    # Print as integer if both inputs were integer-valued
    if result.is_integer():
        print(int(result))
    else:
        print(result)
