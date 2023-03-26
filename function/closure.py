def square(num):
    return num * num


f = square
print(type(f))
print(f(10))

list_name = [1, "apple", f]
print(list_name[-1](10))


def func(func1, parm):
    return func1(parm)


print(func(f, 10))


def return_func():

    def inner_func():
        print("this")
    return inner_func


f = return_func()
print(type(f))
f()


def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(3))



def average():
    nums = []
    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums(5))
print(average_nums(15))