list=[10,20,60,30,20,40,30,60,70,80]
# print(dir(list))
my_list=[]
for i in range(len(list)):
    a=list.count(list[i])
    if list[i] in my_list:
        my_list.remove(list[i]) 
    if a>1:
        my_list.append(list[i])
       
print(my_list)