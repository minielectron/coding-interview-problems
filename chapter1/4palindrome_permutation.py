# Assumptions made: All character are in lower and spaces are ignored.
s = "Tact Coa".lower()

# Create frequency map

m = {}
for x in s: # Order O(N)
    if x != ' ':
        if m.get(x) == None:
            m[x] = 1
        else:
            m[x] +=1 

ispalindrome = True
single = 0

for x,y in m.items(): #O(N)
    if y == 2:
        pass
    elif y == 1:
        single+=1
    else:
        ispalindrome = False
        break

if ispalindrome and (single == 1 or single == 0):
    print("Palindrome string") 
else:
    print("Not palindrome string")   

    # The time complexity is big O(N) and space complexity is O(N)