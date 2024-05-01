s = input('')
p = ''
'''Inverte frase'''
for i in range(1, len(s) +1):
    p += s[-i]

palindromo = False
if s == p:
    palindromo = True
else:
    chars = ''
    for char in s:
        if s.count(char) % 2 != 0:
            if char not in chars:
                chars+= char
    if len(chars) >1:
        palindromo = False
    else:
        palindromo = True

if palindromo:
    print(1)
else:
    print(0)
