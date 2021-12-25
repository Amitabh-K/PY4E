# try:
#     hrs = float(input('enter hours: '))
#     rate = float(input('enter rate: '))
# except:
#     print("Enter Numeric Value")
#
# if hrs <= 40:
#     print(hrs*rate)
# else:
#     print((40*rate) + ((hrs-40)*(rate)*1.5))



# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try:
    num = float(input('enter number between 0.0 to 1.0: '))
except:
    print("Enter Numeric Value")
if num >= 1 :
    print('Should be less than 1.0')
elif num >= 0.9 :
    print('A')
elif num >= .8:
    print('B')
elif num >= .7:
    print('C')
elif num >= .6 :
    print('B')
elif num < .6 and num > 0.0 :
    print('D')
else:
    print('Cannot be negative')
