list1=list(map(int,input("Enter your integer list").split()))
list2=list(map(str,input("Enter your string list").split()))
length=min(len(list1),len(list2))
list3=[]
print(list1,list2)
for i in range(length):
    list3.append((list1[i],list2[i]))
print(list3)
