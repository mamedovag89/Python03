# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

num = int(input("Введите кол-во элементов списка: "))
list = [0] * num
for i in range (len(list)):
    list[i] = int(input(f"Введите {i} элемент списка: " ))
search_num = int (input("\n Введите искомое число: "))
while search_num not in list:
    search_num = int (input("Введите число еще раз: "))
count = 0
for lists in list: 
    if list == search_num:
        count += 1
print(f"Число {search_num} встречается {count} раз")