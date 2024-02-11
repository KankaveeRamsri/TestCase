import string

def caesarCipher(s, k):
    ls = []
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for i in s:
        if i.isupper():
            ls.append(upper[(upper.index(i) + k) % 26])
        elif i.islower():
            ls.append(lower[(lower.index(i) + k) % 26])
        else:
            ls.append(i)
    return ''.join(ls)

