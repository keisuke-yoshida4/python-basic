height_list = [166.5, 168.2, 177.3, 164.9, 172.0, 165.4, 179.2, 170.1]
n = len(height_list)
average = round((sum(height_list) / n), 3)
print(f"平均 avg: {average}")
s2 = 0
for i in height_list:
    s2 += ((i - average) ** 2)
s2 /= n
s2 = round(s2, 2)
s = round((s2 ** 0.5), 2)
print(f"分散 s2: {s2}")
print(f"標準偏差 s: {s}")
z_list = []
for i in height_list:
    z = (i - average) / n
    z_list.append(round(z, 2))
    print(f"身長: {i}, 標準化得点 z: {round(z, 2)}")
cv = s / average
print(f"変動係数 cv: {round(cv, 2)}")
