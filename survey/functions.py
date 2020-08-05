def to_map(grades):
    res = {}
    for grade in grades:
        res[grade["question__category"]] = grade["dsum"]
    return res
