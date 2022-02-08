mylist = []
mylist.append(int(input("Number: ")))
mylist.append(int(input("Number: ")))
mylist.append(int(input("Number: ")))
mylist.append(int(input("Number: ")))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
mylist[0], mylist[3] = mylist[3], mylist[0]
print(mylist)