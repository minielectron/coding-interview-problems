# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

str1 = input().lower()
str2 = input().lower()

def oneEditAway() -> bool:
    found = False
    for x in range(len(str1)):
        if str1[x] != str2[x]:
            if found:
                return False
            found = True
    return found

def oneInsertAway(small, large):
    found =  False
    i = 0 # track small string
    j = 0 # track large string
    while i < len(small) and j < len(large):
        if small[i] != large[j]:
            if (found):
                return False
            found = True
            j+=1
        else:
            i+=1
            j+=1
    return found


if len(str1) == len(str2):
    # One edit/replacement away
    print(oneEditAway())
else:
    if len(str1) < len(str2):
        print(oneInsertAway(str1,str2))
    else:
        print(oneInsertAway(str2,str1))


# Test examples
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false