def palindrome(r):
    e = len(r)-1
    s = 0
    while (s<e):
        if (r[s] != r[e]):
            return False
        s+= 1
        e-= 1
    return True

r=(4,3,5,5,4,3)

if(palindrome(r)):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")