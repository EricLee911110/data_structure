num_counter = int(input())

customerList = []
customerDict = {}
counter3D = []
leavingTime = []
output = []
peopleInQueue = 0

for i in range(0, num_counter):     # Create empty counters
	counter3D.append([])    

while True:
	try:
		customerData = input()
		customerList.append(customerData)
		peopleInQueue += 1
	except:
		break
    


for customer in customerList:
  	customerDict[customer.split(' ')[0]] = [customer.split(' ')[1], customer.split(' ')[2]]

#print("customerList: \n", customerList)
#print("\ncustomerDict: \n", customerDict)
#print("\ncounter3D: \n", counter3D)

idx_in_customer = 0
currentTime = 0

while (peopleInQueue != 0):
	# if customer finish their work
    if currentTime in leavingTime:
        #print("currentTime: ", currentTime)
        
        leavingPeople = []
        for c, counter in enumerate(counter3D):
            for people in counter:
                if people[1] == currentTime:
                    name = people[0]
                    leavingPeople.append([name, c])
        #print("counter3D: \n", counter3D)
        #print("leavingPeople: ", leavingPeople)
        
        for people in leavingPeople:
            leavingPeopleName = people[0]
            leavingPeopleCounter = people[1]
            # remove from counter3D
            counter3D[leavingPeopleCounter].pop(0)
            
            #print("customerDict: ", len(customerDict))

            # append leaving people to output
            output.append(f"{leavingPeopleName} {currentTime} {leavingPeopleCounter}")
            peopleInQueue -= 1

    # if the customer entered the bank
    while currentTime == int(customerList[idx_in_customer].split(' ')[1]):
        if idx_in_customer == -1:
            break

        customerName = customerList[idx_in_customer].split(' ')[0]
        
        #print(customerName)
        duration = int(customerList[idx_in_customer].split(' ')[2])

        if (idx_in_customer < len(customerList)) and idx_in_customer != -1:
            idx_in_customer += 1
        
        if idx_in_customer == len(customerList):
            idx_in_customer = -1

        minPeople = float('inf')
        #print("counter3D inside the function: \n", counter3D)
        for i, e in enumerate(counter3D):
            #print(i, "len(e): ", len(e) , " min: ", minPeople)
            if (len(e) < minPeople):
                minPeople = len(e)
                idx_counter = i
        
        #print("idx_counter: ", idx_counter)
        if len(counter3D[idx_counter]) == 0:
            counter3D[idx_counter].append([customerName, (currentTime + duration)])
            leavingTime.append(currentTime + duration)
        else:
            prev_finish_time = counter3D[idx_counter][minPeople - 1][1]
            counter3D[idx_counter].append([customerName, prev_finish_time + duration])
            leavingTime.append(prev_finish_time + duration)
    
    
    
    
    # current_time add 1 in each loop
    currentTime += 1

#print("counter3D: \n", counter3D)

for e in output:
    print(e)