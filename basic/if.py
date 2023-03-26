age = 200
age_alcohol = 20
age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have a drivers licence")

if not 0 < age < 120:
    print("The vlue is invalid")

balance = 10000000
withdraw = 1300000

# if balance > withdraw:
#     balance -= withdraw
#     print("Your new balance is {}".format(balance))
# else:
#     print("You don't have money")

withdraw_limit = 1000000

if withdraw > withdraw_limit:
    print("The withdrawal limit is {}".format(withdraw_limit))
elif balance > withdraw:
    balance -= withdraw
    print("Your new balance is {}".format(balance))
else:
    print("You don't have money")