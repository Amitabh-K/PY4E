# # try:
# #     hrs = float(input('enter hours: '))
# #     rate = float(input('enter rate: '))
# # except:
# #     print("Enter Numeric Value")

# # if hrs <= 40:
# #     print(hrs*rate)
# # else:
# #     print((40*rate) + ((hrs-40)*(rate)*1.5))



# # fname = input("Enter file name: ")
# # fh = open(fname)
# # lst = list()
# # for line in fh:
# #     words = line.split()
# #     for word in words:
# #         if word not in lst:
# #             lst.append(word)
# # lst.sort()
# # print(lst)

# # stuff = dict()
# # print(stuff.get('candy',-1))

# # if key in counts:
# #     counts[key] = counts[key] + 1
# # else:
# #     counts[key] = 1

# file = input("Enter file:")
# if len(file) < 1 : file = "mbox-short.txt"
# text = open(file)

# max_sender = dict()

# for line in text:
#     line.rstrip()
#     if not line.startswith("From "): continue
#     words = line.split()
#     max_sender[words[1]] = max_sender.get(words[1],0)+1

# largest = None
# latgest_sender = None

# for key in max_sender:
#     if largest is None: largest = max_sender[key]

#     if largest < max_sender[key]:
#         largest = max_sender[key]
#         latgest_sender = key

# print(latgest_sender, largest)


# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# text = open(name)

# maxauthor = dict()

# for line in text:
#     line.rstrip()
#     if not line.startswith("From "): continue
#     words = line.split()
#     maxauthor[words[1]] = maxauthor.get(words[1],0)+1

# largest = None
# largest_author = None

# for key in maxauthor:
#     if largest is None: largest = maxauthor[key]

#     if largest < maxauthor[key]:
#         largest = maxauthor[key]
#         largest_author = key

# print(largest_author, largest)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue

for k,v in hcount.items():                           #k = hour, v = count
    hlst.append((k,v))                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print(k,v)                                       #print counts sorted by hour