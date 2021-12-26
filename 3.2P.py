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

# try:
#     num = float(input('enter number between 0.0 to 1.0: '))
# except:
#     print("Enter Numeric Value")
# if num >= 1 :
#     print('Should be less than 1.0')
# elif num >= 0.9 :
#     print('A')
# elif num >= .8:
#     print('B')
# elif num >= .7:
#     print('C')
# elif num >= .6 :
#     print('B')
# elif num < .6 and num > 0.0 :
#     print('D')
# else:
#     print('Cannot be negative')

#
# def computepay(hrs, rate):
#
#     if (hrs <= 40):
#         pay = ((hrs * rate))
#     else:
#         pay = ((40 + (hrs-40)*1.5)*rate)
#     return print('Pay',pay)
#
#
# hrs = float(input('Please enter hours ' ))
# rate = float(input('Please enter rate ' ))
#
# computepay(hrs, rate)



# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9,41,12,3,74, 15] :
#     if the_num > largest_so_far :
#        largest_so_far = the_num
#     print(largest_so_far, the_num)
#
# print('After', largest_so_far)
#
#
# count = 0
# sum = 0
# print('Before', count, sum)
# for the_num in [9,41,12,3,74, 15] :
#     count = count + 1
#     sum = sum + the_num
#     print(count, sum, the_num)
#
# print('After', count, sum, sum/count)



# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         num_i = int(num)
#     except:
#             print('Invalid input')
#     continue
#     if num_i is None:
#         smallest = num_i
#     elif smallest < num_i:
#         smallest = num_i
#     if num_i is None:
#         largest = num_i
#     elif largest < num_i:
#         largest = num_i
#
#
# print("Minimum", smallest)
# print("Maximum", largest)

# largest = None
# smallest = None
# while True:
#         num = input("Enter a number: ")
# if num == "done" : break
#
# try:
#         num = int(num)
# except:
#         print("Invalid input")
# continue
#
# if largest is None:
#         largest = num
# elif largest < num:
#         largest = num
#
# if smallest is None:
#         smallest = num
# elif smallest > num:
#         smallest = num
#
#
# print(("Maximum is", largest))
# print(("Minimum is", smallest))

# largest = None
# smallest = None
#
    # def max_min(smallest, largest):
    #
    #     while True:
    #         num = input("Enter number: ")
    #
    #         if num == "done":
    #             return(print("Maximum is", largest , "Minimum is", smallest))
    #             break
    #         try:
    #             inp_data = int(num)
    #         except:
    #             print("Invalid input")
    #         continue
    #         if smallest is None:
    #             smallest = inp_data
    #         elif inp_data < smallest:
    #             smallest = inp_data
    #         elif inp_data > largest:
    #             largest = inp_data
    #         return(print("Maximum is", largest , "Minimum is", smallest))
    #
    #
    # max_min(smallest, largest)

# smallest=None
# largest=None
# while True:
#     num=input("Enter number: ")
#     if num =="done":
#         break
#     try:
#         num=int(num)
#     except:
#         print("Invalid input")
#         continue
#     if (smallest==None) or (smallest>num):
#         smallest=num
#     if (largest == None)or (largest < num):
#         largest=num
# print("Invalid input")
# print("Maximum is",largest)
# print("Minimum is",smallest)






# largest = -1
# smallest = None
#
# while True:
#     inp = input('Enter a number: ')
#     print("Maximum is", largest)
#     print("Minimum is", smallest)
#     if inp == 'done' :
#         break
#     try:
#         num = int(inp)
#     except:
#         print('Invalid input')
#         continue
#         if smallest is None:
#             smallest = num
#         if num > largest:
#             largest = num
#         elif num < smallest :
#             smallest = num




largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        num_i = int(num)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = num_i
    elif num_i < smallest :
        smallest = num_i
    elif num_i > largest :
        largest = num_i

print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)






# largest =-1
# num = 0
# smallest = None
# while True:
#     num = input('number: ')
#     if num == "done" :
#         break
#     try:
#         num_i = int(num)
#     except:
#         print('Invalid input')
#     if smallest is None:
#         smallest = num_i
#     elif smallest < num_i:
#         smallest = num_i
#     elif num_i > largest :
#         largest = num_i
#
#
# print("Maximum is", smallest)
# print("Minimum is", largest)
