def getPascalsRow(row_index):
    current_row = [1]

    for level in range(1, row_index + 1):
        next_row = [1] * (level + 1)

        for col in range(1, level):
            next_row[col] = current_row[col - 1] + current_row[col]

        current_row = next_row

    return current_row
# Пример
row_index = 3
print(getPascalsRow(row_index))