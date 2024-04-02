def longest_norepeate_subsequence(seq):
    max_len = 1
    cur_len = 1
    cur_char = seq[0]
    for char in seq[1:]:
        if char != cur_char:
            cur_len += 1
        else:
            cur_len = 1
        max_len = max(max_len, cur_len)
        cur_char = char
    return max_len

seq = "abcddefiighijklmnnabcdefghijklmnoppd"
print(longest_norepeate_subsequence(seq))