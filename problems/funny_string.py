def is_funny_string(s):
    ns = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(ns[i])-ord(ns[i+1])):
            return "Not Funny"
    return "Funny"



