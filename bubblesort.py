def bubblesort(lst, reverse = 0):
    length = len(lst)
    for i in range(0,length-1):
        for j in range(0, length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]

    if reverse:
        lst.reverse()   

    return lst 