string_num=input()
list_num=string_num.split()
lis=[]
for i in list_num:
    if int(i)%3==0:
        lis+=[int(i)]
print(lis)

"""
input:3 10 9 11 18 20
output:[3, 9, 18]

"""
