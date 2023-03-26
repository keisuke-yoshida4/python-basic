# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")
#
# with open("pep8_introduction.txt") as f:
#     print(f.read())

# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)