from functools import lru_cache
import time

print(time.time())
print(time.time()/(60*60*24*365))

@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

before = time.time()
print(fib(30))
after = time.time()
print(f"recursive{after - before:.2f}")

print(time.ctime())
localetime = time.localtime()
print(localetime)
print(localetime.tm_year)
print(f"今の時刻は{localetime.tm_year}年{localetime.tm_mon}月{localetime.tm_mday}日{localetime.tm_hour}時{localetime.tm_min}分です。")
print("今の時刻は{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分です。".format(localetime))

sec = 10
# print(f"{sec}秒待ってください")
# time.sleep(sec)
# print(f"{sec}秒経ちました")

def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after-before:.2f} sec")
    return inner

@timer
def lazy_func(sec):
    print(f"I'm working so hard")
    time.sleep(sec)
    print(f"I'm finally done!")

lazy_func(4)

