def selectionSort(lst, mode):
    """
    Returns the input list sorted in an increasing (default) or a decreasing order

    :param lst: A numeric list.
    :param mode: If -1, the the list is sorted in a decreasing. Otherwise, the list is sorted in an increasing order.
    """
    d = len(lst)
    for i in range(d):
        for j in range(i+1, d):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    if mode == -1:
        lst = lst[::-1]
    return lst


if __name__ == "__main__":
    x = [5, 3, 1, 2, 4]
    print(selectionSort(x, mode=0))  # any value in the `mode` argument except `-1` will do
    print(selectionSort(x, mode=-1))
