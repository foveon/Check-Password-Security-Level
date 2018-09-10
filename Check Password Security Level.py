
# Code to check password security level
#
# Low：
#   1. Only numbers or alphabet letters
#   2. Password length less than 8 characters
#
# Medium：
#   1. Includes Numbers, Symbols, Capital Letters any two combinations
#   2. Password length at least 8 characters
#
# High：
#   1. Includes Numbers, Symbols, Capital Letters all three combinations
#   2. Password start with letters
#   3. Password length at least 16 characters

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('Please input the password：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0) :
    passwd = input("The password is empty or space,please input again：")
    length = len(passwd)

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0

# if symbols are included
for each in passwd:
    if each in symbols:
        flag_con += 1
        break
    
# if letters are included
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# if numbers are included
for each in passwd:
    if each in nums:
        flag_con += 1
        break    

# print result
while 1 :
    print("The security level is：", end='')
    if flag_len == 1 or flag_con == 1 :
        print("Low")
    elif flag_len == 3 and flag_con == 3 and (passwd[0] in chars):
        print("High")
        print("Well done!")
        break
    else:
        print("Medium")

    print("According to the traditional advice—which is still good—a strong password:\n\
    \t1. Includes Numbers, Symbols, and Letters\n\
    \t2. Starts with letters\n\
    \t3. Has 16 Characters, Minimum")
    break
