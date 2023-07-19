
#1 Написать код для функции sum(),
# которая на вход принимает массив,
# а возвращает сумму значений массива
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


#2 Написать рекурсивную функцию,
# принимает массив,
# а возвращет сумму значений массива
def sum2(list):
    if list == []: #базовый случай
        return 0
    return list[0] + sum2(list[1:]) # рекурсивная часть с применением среза списка, чтобы производить суммирование остального списка


#3 Написать код. чтобы найти наибольшее число в списке
# с использованием вложенного цикла

def def_biggest_num(list):
    current_num = 0
    compared_num = 0
    biggest_num = 0
    for i in range(len(list)):
        current_num = list[i]
        for j in range(len(list)):
            compared_num = list[j]
            if current_num > biggest_num:
                biggest_num = current_num

    return biggest_num


#4  Написать код с использованием рекурсии, чтобы найти наибольшее число в списке

def def_biggest_num2(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    return list[0] if list[0] > def_biggest_num(list[1:]) else def_biggest_num(list[1:])


#4  Написать код с чтобы найти наибольшее число в списке с использованием встроенных методов списка

def def_biggest_num3(list):
    return max(list)


#5  Написать код с чтобы найти наибольшее число с используя по минимуму переменных

def def_biggest_num4(list):
    biggest_num = list[0]
    if list == []:
        return None
    for num in range(len(list)):
        if list[num] > biggest_num:
            biggest_num = list[num]
    return biggest_num
