def greeting(func):
    def inner_greeting(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("nice to meet you")
    return inner_greeting


@greeting
def say_name(name):
    print(f"I'm {name}")


@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name = greeting(say_name)
say_name("jiro")
say_name_and_origin("Taro", "Tokyo")
