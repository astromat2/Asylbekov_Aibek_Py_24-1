def binary_search(target, lst):
    l = 0
    r = len(lst)
    while l + 1 < r:
        m = (l + r) // 2
        if lst[m] == target:
            l = m
            r = m
            break
        elif lst[m] > target:
            r = m
        else:
            l = m + 1
    if lst[l] == target:
        print(f'Цифра найдена под индексом {l}.')
    else:
        print(f'Цифра не найдена.')


binary_search(9, [1, 2, 3, 6, 7, 8, 10])
binary_search(3, [1, 3, 6, 7, 8, 9, 10])

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

print(bubble_sort([5,54, 3, 5, 5, 7,3, 4]))