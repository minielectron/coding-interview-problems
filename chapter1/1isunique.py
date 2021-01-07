
# Solution 1: Using sorting this can take upto nlogn, depends on sorting.
str1 = "random"
chars = sorted(str1)

isunique = True
for i in range(len(chars)-1):
    if chars[i] == chars[i+1]:
        isunique = False
        break

if isunique:
    print("String is unique")
else:
    print("String is not unique")

# Solution: Using map, this will take O(n) time complexity and O(n) space complexity,
# where is length of input string, the space complexity will never cross 128 if unicode. 
# so it's contant and can be considred as O(1).

str2 = "randomr"
isunique2 = True
ht = {}
for c in str2:
    if ht.get(c) == None:
        ht[c] =  1
    else:
        isunique2= False
        break

print(isunique2)

# What is ascii and what is unicode? read about it and then you can write more meaningful codes.
