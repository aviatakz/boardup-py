def average_list(objects):
    map_self = {}
    list_self = {}
    for grade in objects:
        category = grade.question.category.pk
        if category in map_self:
            map_self[category] += 1
            list_self[category] += grade.value
        else:
            map_self[category] = 1
            list_self[category] = grade.value

    result = {}
    for key, value in map_self.items():
        result[key] = list_self[key] / value

    return result
