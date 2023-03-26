s = lambda x: x * x
print(s(3))


def power(exponent):
    lambda base: base ** exponent


numbers = [5, 2, 6, 43, 4, 36, 67, 2]

# def filterfunc(num):
#     return not num % 2 == 0
    #     return False
    # else:
    #     return True


filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))
