print(not True)  #Логическое НЕ
print(not False)

cond1 = 0 < 1 #Логическое И
cond2 = 1 < 4
print(cond1 and cond2)
cond3 = 't' in "python"
cond4 = 't' in "django"
print(cond3 and cond4)

print(('t' in "python") or ('t' in "django")) #Логическое ИЛИ

def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))

def is_leap_year(x):
 return (x % 400 == 0) or ( x % 4 == 0) and ( x % 100 != 0)
x = int(input("Введите год:"))
print(is_leap_year(x))

print(list(str(123456789))) #У нас есть послоедоватлеьность чисел. Превратим её сразу в строку и сразу в список
print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9']))) #Тут мы первели каждый элемент списка обратно в число
list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit) #Проверяем есть ли среди них цифра 5

print('5' in str(123456789)) #А можно было ещё прощё

N = (1, 2, 3, 4, 5, 6, 7, 8, 9) #Можно и так проверить есть ли в последовательности нужные нам цифры
print('3' in str(N) and '7' in str(N))

a = [1, 2, 3]
print(id(a))
b = a #Приравниваем и в итоге они эквиваленты ведь их id один и тот же потому что СПИСОК это ИЗМЕНЯЕМЫЙ ээлемент
print(id(b))
print(a is b) #проверямем на ЭКВИВАЛЕНТНОСТЬ

a = [1, 2, 3] #Хоть и значения у обеих переменных одни НО они не эквивалентны
b = [1, 2, 3] #Мы их не приравняли друг к другу
print(a == b)  #Проверим равны ли
print(a is b) #Проверим эквивалентны ли
