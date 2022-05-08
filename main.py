# Задание 1

a=0
while a<4:
    print (a , '0000')
    a += 1


# Задание 2

a2=0
while a2<10:

    number = input('Введите число: ')
    while not number.isdigit() :
        number = input('Введите число: ')

    a2 += 1
    if a2 == 10:
        print('Вы ввели число', a2 , 'раз. Больше не надо' )
    elif a2 == 1 or a2 >= 5:
        print('Вы ввели число', a2, 'раз')
    else:
        print('Вы ввели число', a2, 'раза')


# Задание 3

n=1
summa=0
while n <= 100:
    #print(n)
    summa=summa+n
    n += 1
print (summa)


# Задание 4

z=1
factorial=1
while z <= 10:
    factorial=factorial * z
    z += 1

print(factorial)

# Задание 5

x = input('Введите число: ')
while not x.isdigit():
    x = input('Введите число: ')
x_lenght = len (x)
index = 0
while index != x_lenght:
    print (x[index])
    index += 1