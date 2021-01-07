# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

ins = input() 
input_with_marker = ins + "0" # Took o as marker 
count = 1
result = ""
for i in range(len(input_with_marker)-1):
    if input_with_marker[i] == input_with_marker[i+1]:
        count+=1
    else:
        result+=f"{input_with_marker[i]}{count}"
        count = 1

if len(result) < len(ins):
    print(result)
else:
    print(ins)

# Time complexity = O(N)