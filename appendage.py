list1=[1,2,[3,4,5],6,[7,[8,9]],10,[11,[12],13],14]
list2=[]
def flatten(list1):
    for i in range(len(list1)):
        if(type(list1[i])==list):
            flatten(list1[i])
        else:
            list2.append(list1[i])
flatten(list1)
print(list2)
