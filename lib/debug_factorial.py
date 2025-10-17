def factorial(n):
    product = n
    print(f"At the start, product = {product} & n = {n}")
    while n > 1:
        n -= 1
        print(f"n is now {n}")
        print(f"Product = product * n = {product} * {n}")
        product *= n
        print(f"Product = {product}")
        print("")

    return product

print(f"""
Running: factorial(5)
Expected: 120`
Actual: {factorial(5)}
""")