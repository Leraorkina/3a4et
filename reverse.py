def reverseStr(input_str, chunk_size):
    char_list = list(input_str)

    for start_index in range(0, len(char_list), 2 * chunk_size):
        char_list[start_index:start_index + chunk_size] = reversed(char_list[start_index:start_index + chunk_size])

    return ''.join(char_list)
# Пример 
input_str = "abcdefg"
chunk_size = 2
print(reverseStr(input_str, chunk_size))