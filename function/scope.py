def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")


print_name_local()


age = 30


def print_age():
    global age
    age = 20
    print(f"I'm {age} years old")

print_age()
print(age)
