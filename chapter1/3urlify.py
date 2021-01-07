url = input()
urlchars = [x for x in url]
for x in range(len(urlchars)): # O(N)
    if urlchars[x] == ' ':
        urlchars[x] = '%20'

print("".join(urlchars))

# Time complexity O(N) and space complexity is also O(N)