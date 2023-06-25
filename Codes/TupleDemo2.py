print("Demonstration of Tuple")

tup = (11,"Marvellous",3.14,51,"Infosystems")

print(tup)
print(tup[0])
print(tup[1])
print(tup[1:])
print(tup[:2])
print(tup[1:2])

# tup[1] = "marvellous"       Not allowed to change contents

print(len(tup))
print("Marvellous" in tup)

del tup

# *** Properties of tuple ***
# Heterogeneous
# Ordered
# Indexed
# immutable
# Allows duplicate