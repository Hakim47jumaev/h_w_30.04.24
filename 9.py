list1=[10,20,30,40,50,60,70,80,90,100]
my_list=[]
for i in range(len(list1)):
    if i%2!=0:
        my_list.append(list1[i]) 
print(my_list)