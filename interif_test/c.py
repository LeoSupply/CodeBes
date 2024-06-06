num = input('')

if len(num) <= 20 and len(num) >= 1:
    soma_par = 0
    soma_impar = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            soma_par+=i
        else:
            soma_impar+=i


    if soma_par % 3 == 0:
        print('S')
    else:
        print('N')
    if soma_impar % 3 ==0:
        print('S')
    else:
        print('N')
