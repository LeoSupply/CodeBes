S = input('')
P = ''
'''Inverte frase'''
for i in range(1, len(S) +1):
    P += S[-i]

palindromo = False
if S == P:
    palindromo = True
else:
    chars = ''
    for char in S:
        if S.count(char) % 2 != 0:
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

# abcdabcdd