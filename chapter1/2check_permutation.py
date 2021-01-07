# str1 = input()
# str2 = input()

str1 = "This is having spaces     "
str2 = "This is having spaces"
print(len(str1))
print(len(str2))

perm = True
if len(str1) == len(str2):
    for c in str1:
        if c not in str2:
            perm = False
            break 
else:
    perm = False
    
if perm: 
    print("It's permutation")
else:
    print("It's not permutation")

# Second solution: If the string are permutation then if we sort it, both string should be equal.

s = sorted(str1) 
t = sorted(str2)

if s == t:
    print("It's permutation")
else:
    print("It's not permutation")
