def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr =myrange(10)
# print(type(mr))
#
# for i in mr:
#     print(i)
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))


for i in mr:
    print(i)


def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


for i in even(10):
    print(i)

print("=" * 30)
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))
print(id(even_gen))
print(id(iter(even_gen)))