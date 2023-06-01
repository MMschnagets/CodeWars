def permutations(s):
    list_temp = [item for item in s]
    list_base = list(set(list_temp))
    dict_number = {key_letter: list_temp.count(key_letter) for key_letter in list_base}
    list_to_return = list_base.copy()
    for index in range(1, len(s)):
        list_temp = list()
        for item_return in list_to_return:
            list_temp.extend([item_return + item for item in list_base if item_return.count(item) < dict_number[item]])
        list_to_return = list_temp
    return list_to_return


print(permutations('aabb'))
