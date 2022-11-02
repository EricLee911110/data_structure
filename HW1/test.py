num_counter = int(input())

customerList = []
customerDict = {}
counter3D = []
leavingTime = []
output = []

for i in range(0, num_counter):     # Create empty counters
    counter3D.append([])    

while True:
    customerData = input()
    if customerData == '':
        break
    customerList.append(customerData)


for customer in customerList:
    customerDict[customer.split(' ')[0]] = [customer.split(' ')[1], customer.split(' ')[2]]

#print("customerList: \n", customerList)
#print("\ncustomerDict: \n", customerDict)
#print("\ncounter3D: \n", counter3D)

idx_in_customer = 0
idx_out_customer = 0
currentTime = 0

def theLeastNumberCounter():
    minPeople = float('inf')
    #print("counter3D inside the function: \n", counter3D)
    for i, e in enumerate(counter3D):
        #print(i, "len(e): ", len(e) , " min: ", minPeople)
        if (len(e) < minPeople):
            minPeople = len(e)
            min_idx_counter = i
    
    return min_idx_counter, minPeople

def whoIsLeaving(timeNow):
    leavingList = []
    for c, counter in enumerate(counter3D):
        for people in counter:
            if people[1] == timeNow:
                name = people[0]
                leavingList.append([name, c])

    return leavingList


while (len(customerDict) != 0):
    # if the customer entered the bank
    if currentTime == int(customerList[idx_in_customer].split(' ')[1]):
        
        customerName = customerList[idx_in_customer].split(' ')[0]
        if (idx_in_customer < len(customerList) - 1):
            idx_in_customer += 1
        #print(customerName)
        customerTime = customerDict[customerName]

        idx_counter, minPeople = theLeastNumberCounter()
        #print("idx_counter: ", idx_counter)
        if len(counter3D[idx_counter]) == 0:
            counter3D[idx_counter].append([customerName, currentTime + int(customerTime[1])])
            leavingTime.append(currentTime + int(customerTime[1]))
        else:
            prev_finish_time = counter3D[idx_counter][minPeople - 1][1]
            counter3D[idx_counter].append([customerName, prev_finish_time + int(customerTime[1])])
            leavingTime.append(prev_finish_time + int(customerTime[1]))
    
    
    
    # if customer finish their work
    if currentTime in leavingTime:
        #print("currentTime: ", currentTime)
        leavingPeople = whoIsLeaving(currentTime)
        #print("counter3D: \n", counter3D)
        #print("leavingPeople: ", leavingPeople)
        
        for people in leavingPeople:
            leavingPeopleName = people[0]
            leavingPeopleCounter = people[1]
            # remove from counter3D
            counter3D[leavingPeopleCounter].pop(0)
            
            # remove from customerDict
            del customerDict[leavingPeopleName]
            #print("customerDict: ", len(customerDict))

            # append leaving people to output
            output.append(f"{leavingPeopleName} {currentTime} {leavingPeopleCounter}")

    # current_time add 1 in each loop
    currentTime += 1

#print("counter3D: \n", counter3D)

for e in output:
    print(e)