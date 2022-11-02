# counters = []
# counters.append([])
# counters.append([])
# counters[0].append(["jack", 12])
# counters[1].append(["Mary", 11])
# counters[1].append(["Susan", 2])
# print(counters)

# minPeopleCounter = float('inf')
# for i, e in enumerate(counters):
#     if (len(e) < minPeopleCounter):
#         minPeopleCounter = i

# print(minPeopleCounter)

# counters[1].pop(0)
# print(counters[1][0])
# print(counters)


# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# b = [1,4,7]
# thingsToDelete = []

# for r, row in enumerate(a):
#     for c, column in enumerate(row):
#         if column in b:
#             thingsToDelete.append(r)

# print("things to be delete:", thingsToDelete)
# for object in thingsToDelete:
#     a[object].pop(0)

# print(a)


# a = [1,2,3]

# try:
#     if 1 in a:
#         print("here")

# except:
#     pass

# print("we are done here")


# a = {"Eric": 1}
# del a["Eric"]
# print(len(a))


x = 0
while x < 5:
    
    if x == 3:
        break
    print(x)
    x += 1