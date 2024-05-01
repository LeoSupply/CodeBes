n = int(input(''))
m = int(input(''))

vivos = []
mortos = []

for i in range(1, n+1):
    vivos.append(i)

#Forma 1
i = 1
while len(vivos) != 1:
    mortos.append(vivos[i])
    del vivos[i]
    i += 1
    i %= len(vivos)

#Forma 2
# i = 1
# while len(vivos) != 1:
#     if i == (len(vivos)-1):
#         mortos.append(vivos[i])
#         del vivos[i]
#         i = 1
#     elif i > (len(vivos)-1):
#         i = 0
#         mortos.append(vivos[i])
#         del vivos[i]
#         i+=1
#     else:
#         mortos.append(vivos[i])
#         del vivos[i]
#         i+=1

print(f"Morte {m}:", mortos[m-1])
print("Sobrevivente:", vivos[0])
