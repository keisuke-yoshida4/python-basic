import re
#
# email = "myemail@gmail.com"
# print("@" in email)
#
# matched = re.search('@\w+\.', email)
# if matched:
#     print(matched)
#     print("Matched")
# else:
#     print("Not found")
#
#
# print(re.search('[abc]', 'apple'))
# print(re.search('[0-9]', '7'))
# print(re.search('^[0-9]', '5abc'))
# print(re.search('^[0-9]{4}', '2021/3'))
# print(re.search('^[0-9]{2,4}', '21/3'))
# print(re.search('[0-9]{2}$', '21/3/31'))
# print(re.search('a*b', 'b')) #0回以上
# print(re.search('a+b', 'aaaab'))
# print(re.search('ab?d', 'abd'))
# print(re.search('abc|012', '012'))
# print(re.search('te(s|x)t', 'text'))
# print(re.search('h.t', 'hat'))
# print(re.search('h\.t', 'h.t'))
# print(re.search('h\wt', 'h2t'))

# pattern = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
# while True:
#     tosi = input("あなたの生年月日を入力してください (yyyy/mm/dd)")
#     result = re.search(pattern, tosi)
#     if result:
#         print("OK")
#         break
#     else:
#         print("入力内容が間違っています。再度入力してください。")

pattern_email = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("emailを入力してください")
    result = re.search(pattern_email, email)
    if result:
        print("OK")
        break
    else:
        print("入力内容が間違っています。再度入力してください。")