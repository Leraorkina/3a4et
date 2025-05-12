class FlattenIterator:
    def __init__(self, nested):
        self.path = [(nested, 0)]
    def __iter__(self):
        return self

    def __next__(self):
        while self.path:
            current_list, idx = self.path[-1]

            if idx >= len(current_list):
                self.path.pop()
                continue

            self.path[-1] = (current_list, idx + 1)
            element = current_list[idx]

            if isinstance(element, list):
                self.path.append((element, 0))
            else:
                return element

        raise StopIteration

# Пример
nested_data = [1, [2, 3], [4, [5, 6]], 7]
for value in FlattenIterator(nested_data):
    print(value)
