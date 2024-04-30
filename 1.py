list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sub_list=['h','i','j']
for i in range(len(sub_list)):
   list1[2][1][2].append(sub_list[i])
print(list1)