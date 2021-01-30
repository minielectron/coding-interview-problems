# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

url = input()
urlchars = [x for x in url]
for x in range(len(urlchars)): # O(N)
    if urlchars[x] == ' ':
        urlchars[x] = '%20'

print("".join(urlchars))

# Time complexity O(N) and space complexity is also O(N)