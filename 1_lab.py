from functools import reduce

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]

inv_num = list(map(lambda x: 1/x, num))

f_num = list(filter(lambda x: x < 1, inv_num))

avg = reduce(lambda x, y: x + y, f_num) / len(f_num)

print("\nОбратное значение: ", inv_num)
print ("\nЗначение меньше 1: ", f_num)
print("\nСреднее арифметическое", avg)
