string_num=input()
num_list=string_num.split()
small=999999
for i in num_list:
    if int(i)<small:
        small=int(i)
print(small)

"""
input:54 10 15 24 7 12
output:7
"""
