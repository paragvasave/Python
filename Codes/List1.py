Values = [10.20,20,30,40]
print(Values)           #List values
print(type(Values))
print(len(Values))

Values.insert(2,11)
print("Data after insertion : ",Values)

Values.insert(15,89)
print("Data after insertion 15 is ",Values)
print("Size of list after insertion 15 : ",len(Values))

Values.append(50)
print("Data after append : ",Values)

Values.remove(20)
print("Data after append : ",Values)

Values.append(40)
print("Data after append : ",Values)

print(type(Values[0]))

print(Values[0])
print(Values[1])
print(Values[2])
print(Values[3])