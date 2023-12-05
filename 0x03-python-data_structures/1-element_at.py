def element_at(my_list, idx):
    idx = my_list.index(idx)
    length = len(my_list)
    if idx < 0:
        return None
    elif idx >= length:
        return None
    else:
        return my_list[idx]
