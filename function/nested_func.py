def outer():
    def inner():
        print("This is innner function")
    inner()

outer()

