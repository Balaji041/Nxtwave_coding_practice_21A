string=input()
split_string=string.split()
string=""
for i in range(len(split_string)):
    string+=split_string[i][2]
print(",".join(string))

"""
input:Being More Productive
output:i,r,o
"""
