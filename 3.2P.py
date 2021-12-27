try:
    hrs = float(input('enter hours: '))
    rate = float(input('enter rate: '))
except:
    print("Enter Numeric Value")

if hrs <= 40:
    print(hrs*rate)
else:
    print((40*rate) + ((hrs-40)*(rate)*1.5))



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)