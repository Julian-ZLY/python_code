
# -*- coding:utf8 -*-


'''冒泡排序'''
list_01 = [3, 4, 2, 6, 9, 1]

def order_by_list(list_values):
    for i in range(len(list_values) - 1, len(list_values)):
        for j in range((i + 1),len(list_values)):
            if list_values[i] > list_values[j]:
                list_values[i], list_values[j] = list_values[j], list_values[i]
    return list_values


new_list = order_by_list(list_01)
print(new_list)