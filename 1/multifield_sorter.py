
def multi_level_sort_pythonic(records, priorities):
    return sorted(records, key=lambda x: tuple(
        -x[field] if reverse else x[field] for field, reverse in priorities
    ))

if __name__ == '__main__':

    test_data = [
        {'a': 1.0, 'b': 3.0, 'c': 2.0},
        {'a': 1.0, 'b': 2.0, 'c': 3.0},
        {'a': 2.0, 'b': 1.0, 'c': 1.0},
        {'a': 1.0, 'b': 3.0, 'c': 1.0}
    ]

    result = multi_level_sort_pythonic(test_data, [('a', True), ('b', True), ('c', True)])
    for item in result:
        print(item)

