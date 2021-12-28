def merge(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result


if __name__ == '__main__':
    merge(['a', 'b'], [1, 2], [True, False])  # [['a', 1, True], ['b', 2, False]]
    merge(['a'], [1, 2], [True, False])  # [['a', 1, True], [None, 2, False]]
    merge(['a'], [1, 2], [True, False], fill_value='_')
