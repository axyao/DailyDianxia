import pickle
import random
import constants

mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "sdfsdfsdfsd"]
myQueue = []

# with open(constants.queueFileName, "wb") as f:
#     pickle.dump(myQueue, f)
    
with open(constants.queueFileName, "rb") as f:
    myNewQueue = pickle.load(f)

print(myNewQueue)

while 1:
    randItem = random.choice(mylist)
    if randItem in myNewQueue:
        print("can't use randItem, it's already in queue: ", randItem)
    else:
        print("safely add randItem to queue")
        if len(myNewQueue) >= constants.queueSize:        
            popped = myNewQueue.pop(0)
            print("popped: ", popped)
        myNewQueue.append(randItem)
        break

print(myNewQueue)

with open("list_queue_test.pkl", "wb") as f:
    pickle.dump(myNewQueue, f)
