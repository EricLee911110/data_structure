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

idx_customer = 0
current_time = 0
while(len(customerDict) != 0):
    # if the customer entered the bank
    if ()
    customerName = customerList[idx_customer].split(' ')[0]
    
    # if finished
    del customerDict[customerName]
    idx_customer += 1

    # current_time add 1 in each loop
    current_time += 1

