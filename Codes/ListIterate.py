
Data = [11,21,51,101]
print("___________________________________________")

print("Output using for")
for no in Data:
    print(no,end=" ")

print("\n___________________________________________")

print("Output using for with index")
for i in range(0,len(Data),1):
    print(Data[i],end=" ")

print("\n___________________________________________")

print("Output using for while using index")

i=0
while(i!=len(Data)):
    print(Data[i],end=" ")
    i+=1                        #i=i+1
print("\n___________________________________________")


    