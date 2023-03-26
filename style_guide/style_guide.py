x = 1
y = 1


# 関数の引数の「=」にはスペース不要
def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# operatorの周りにスペース１個、operatorにpriorityがある場合はスペースをなくす
x = x + 1
x += 1
x = x*2 -1
a = x*x + y*y
c = (a+1) * (a-1)

# カンマの後にはスペースを入れる
range(1, 11)

# カンマの後に閉じ括弧がくる場合はスペース不要
foo = (0,)

Files = [
    "setup.cfg",
    "tox.ini",
    "tex.ini",
]

 # 行の折り返し
 foo = long_function_name(var_one, var_two,
                          var_three, var_four)

 foo = long_function_name(var_one, var_two,
    var_three, var_four)


 def long_function_name(
         var_one, var_two, var_three,
         var_four)


# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できます")

a = 100000000000000000 \
    + 100000000000000000 \
    + 100000000 \
    + 100000