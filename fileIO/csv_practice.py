import csv

# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[1])

# with open("example.csv") as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line["Country"])

# with open("sample.csv", mode='w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['value1', 'value2'])
#     writer.writerow(['value3', 'value4'])

with open("sample.csv", mode="w") as f:
    writer = csv.DictWriter(f, ['cal1', 'cal2'])
    writer.writeheader()
    writer.writerow({"cal1": "value1", "cal2": "value2"})
    writer.writerow({"cal1": "value3", "cal2": "value4"})
