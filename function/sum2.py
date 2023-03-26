average = 60
s = 15

z_list = [92, 78]
for i in z_list:
    z = (i - average) / s
    print(f"得点: {i}, 標準化得点 z: {z}")
cv = s / average
print(f"変動係数 cv: {round(cv, 2)}")
