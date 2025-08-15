# def outer():
#     x = "outer"

#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print(x)

# outer()  # Output: inner

x = "global"

def outer():
    x = "enclosing"

    def inner():
        global x
        x = "local"
        print(x)
    inner()

outer()
print(x)  # Output: local