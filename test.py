num_counter = int(input())

customerList = []
customerDict = {}
counterDict = {}

for i in range(0, num_counter):     # Create empty counters
    counterDict[str(i)] = []    

while True:
    customerData = input()
    if customerData == '':
        break
    customerList.append(customerData)


for customer in customerList:
    customerDict[customer.split(' ')[0]] = [customer.split(' ')[1], customer.split(' ')[2]]

print("customerList: \n", customerList)
print("\ncustomerDict: \n", customerDict)
print("\ncounterDict: \n", counterDict)

idx_in_customer = 0
idx_out_customer = 0
currentTime = 0

while (len(customerDict) != 0):
    # if the customer entered the bank
    if True:
        pass 

    customerName = customerList[idx_in_customer].split(' ')[0]
    idx_in_customer += 1
    print(customerName)
    customerTime = customerDict[customerName]
    
    
    # if finished
    del customerDict[customerName]
    idx_out_customer += 1

    # current_time add 1 in each loop
    currentTime += 1

