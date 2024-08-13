def uslovija(i):
    counter2 = 0
    if isinstance(i, int):
        counter2 += i
        return counter2
    elif isinstance(i, str) or len(i) == 0:
        counter2 += len(i)
        return counter2
    else:
        return counter2 + calculate_structure_sum(i)


def calculate_structure_sum(data_structure):# Здесь я сделал так, чтобы мы не ограничивались одним списком со списками, можно добавить их сколько угодно
    counter = 0
    if type(data_structure) == None:
        return 0
    elif isinstance(data_structure, int):
        counter += data_structure
    elif isinstance(data_structure, str):
        counter += len(data_structure)
    elif isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        for i in data_structure:
            counter += uslovija(i)
    elif isinstance(data_structure, dict):
        for i, j in data_structure.items():
            counter += uslovija(i)
            counter += uslovija(j)
    return counter


data_structure = [[
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]]

# попробуйте это тоже (Ответ 246, проверял на калькуляторе лично)
# data_structure = [(1,2,3,'HFkidnvi'),{'Bob':123 , 'Mem':[1,'kek']},[[
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]]]

result = calculate_structure_sum(data_structure)
print(result)
