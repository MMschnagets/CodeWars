def first_non_repeating_letter(s: str) -> str:
    s_only_lower = s.lower()
    list_tmp = [s_only_lower.count(item) for item in s_only_lower]
    if 1 not in list_tmp:
        return ''
    else:
        return s[list_tmp.index(1)]


print(first_non_repeating_letter("sTreSS"))
