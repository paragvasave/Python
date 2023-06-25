Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}
print("Data of dictionary : ",Batches)

print("Data traversal using for each loop")
for x in Batches:
    print(x)

print("")

print("Data traversal using for loop")
for x in Batches:
    print(x,Batches[x])

print("")

print("Data traversal using for loop")
for x in Batches:
    print(x,Batches.get(x))

print("")

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

print("")

valuesBatches = Batches.values()
print(type(valuesBatches))
print(valuesBatches)


