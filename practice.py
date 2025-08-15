def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)

outer()  # Output: inner
