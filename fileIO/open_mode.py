# with open("writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text")

# with open("writing_file.txt", mode='r+') as f:
#     f.write("You can write and read with r+ mode!!")
#     print(f.read())
#     f.write("This should be the last sentence")
#     print(f.read())

# with open("writing_file.txt", mode='w+') as f:
#     print(f.read())
#     f.write("You can write and read with w+ mode!!")
#     f.seek(0)
#     print(f.read())

with open("writing_file.txt", mode='a+') as f:
    print(f.read())
    f.write("\nYou add sentences to the last of the file content with a+ mode")
    f.seek(0)
    print(f.read())