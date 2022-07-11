s = input()
sl = s.lower()
p = sl[::-1]
if sl == p:
    print('Palindrome')
else:
    print('Not a Palindrome')