Mylist=["Ahmed","Akram",10,7.5,True] # Can Contain Different Types

print(Mylist) #Print Whole List
#Indexing
print(Mylist[0]) #First Item =Ahmed
print(type(Mylist[0])) #->>String
print(Mylist[-1]) #print last Item =True
print(type(Mylist[-1])) # Boolean
print(Mylist[2]) # print Second Item =10
print(type(Mylist[2])) #Integer
print(Mylist[-2]) # 7.5
print(type(Mylist[-2])) # Float

#Slicing -->>End Not Included and O/P =List
print(Mylist[2:4]) # [10,7.5]
print(Mylist[:3]) #["Ahmed","Akram",10]
print(Mylist[1:])#["Akram",10,7.5,True]
print(Mylist[:]) #Whole List
print(Mylist[-4:-1]) #important-->>End Not Included

print(Mylist[::1]) #Whole Data
print(Mylist[::2]) #Skip one Item
print(Mylist[::3]) #Skip Two Items

# print(Mylist[5])# IndexError: list index out of range

#Edit List

Mylist[0]=500
Mylist[3]=False
Mylist[-1]="Omar"
print(Mylist) #[500, 'Akram', 10, False, 'Omar']

Mylist[0:3]=["Ahmed","Mostafa","Ali","Moha",112]
print(Mylist) 
Mylist[0:3]=["Ahmed","Mostafa"]
print(Mylist) 
Mylist[0:3]=[] #Will Left The Place Of Them Empty
print(Mylist)  

#Check Item In List Or not By Keyword "in"

Thislist=["Ahmed",100,"Akram","Shimaa",200,"Aya","Zeyad"]

if "Zozo" in Thislist:
    print("Yes it is presents!")
else:
    print ("No it is not present")

if 100 in Thislist:
    print("Yes it is presents!")
else:
    print ("No it is not present")

if 10.0 in Thislist:
    print("Yes it is presents!")
else:
    print ("No it is not present")

L1=["Ahmed","Osama","Akram","Zeyad","Ali","Omar"]
del L1[2]
print(L1)
del L1[2:6]
print(L1)