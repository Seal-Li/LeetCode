def merge_k_sorted_arrays(arrays):
    k = len(arrays)
    array_lengths = [len(subarray) for subarray in arrays]
    positions = [0 for _ in range(k)]
    merged_array = []

    while True:
        min_value = float('inf')
        min_index = -1
        for i in range(k):
            if positions[i] != "end":
                if arrays[i][positions[i]] < min_value:
                    min_value = arrays[i][positions[i]]
                    min_index = i

        if min_index == -1:
            break

        merged_array.append(min_value)
        positions[min_index] += 1

        if positions[min_index] == array_lengths[min_index]:
            positions[min_index] = "end"

    return merged_array


# 测试示例
arrays = [[1, 2, 3], [2, 3, 4], [3, 4, 5, 6]]
print(merge_k_sorted_arrays(arrays))
