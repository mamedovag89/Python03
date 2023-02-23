# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5
num = int(input("Введите кол-во элементов списка: "))
list = [0] * num
for i in range (len(list)):
    list[i] = int(input(f"Введите {i} элемент списка: " ))
num = int (input("\n Введите число: "))
while num == list[i]:
    i += 1
seach_num = list[i]

for lists in list:
    if lists != num:
        if abs(lists - num) < abs(seach_num - num):
            seach_num = lists
print(f"Ближайщее число к числу {num} это {seach_num}")