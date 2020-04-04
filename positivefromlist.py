#declare an empty list
list[]
#inputting elements to the list
n=int(input("enter number of elements in the list: "))
for i in range(0,n):
    a=int(input("enter element: "))
    list.append(a)
    list1=list
list1
list2=list1
#printing positive elements from the list
for i in list1:
    if i>0:
        print(i)
#removing positive elements from the list
for j in list2:
    if j<0:
        list2.remove(j)
print(list2)
