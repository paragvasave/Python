print("Demonstration of List")
Batches = ["PPA","LB","Angular","Python"]

print(Batches)
print("Batches[0]",Batches[0])
print("Batches[1]",Batches[1])
print("Batches[-1]",Batches[-1])
print("Batches[-2]",Batches[-2])
print("Batches[-3]",Batches[-3])
print("Batches[1:]",Batches[1:])
print("Batches[:3]",Batches[:3])


# we can store homogenious data
data1 = [21,"Hello",12.19]
print(data1)
data2 = [11,"Infosystem",6.10]
#We can create list of list
combined = [data1,data2]
print(combined)


# There are mulitple methods that we can use to manipulate list

Batches.insert(2,"LSP")
print(Batches)

Batches.append("MERN")
print(Batches)

Batches.remove("LSP")
print(Batches)

Batches.pop()
print(Batches)

Batches.pop(2)
print(Batches)

del Batches[1:]
print(Batches)

Batches.extend(["LB","Mern","Python","Angular"])
print(Batches)

Batches.sort()
print(Batches)

# *** Properties of list ***
# Heterogeneous
# Ordered
# Indexed
# Mutable
# Allows duplicate