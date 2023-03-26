
text = ""
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

text_list = []
for i in range(1, 11):
    text_list.append((str(i)))

text = "-".join(text_list)
print(text)

name1,name2,name3,name4, name5 = '', '', 'tanaka', 'suzuki', 'sato'
selected_name = name1 or name2 or name3 or name4 or name5
print(selected_name)

