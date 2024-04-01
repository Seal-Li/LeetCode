# 最长连续字符序列
def longest_consecutive_char(s):
    max_char = s[0]
    max_len = 1
    cur_char = s[0]
    cur_len = 1

    for char in s:
        if char == cur_char:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_char = cur_char
        else:
            cur_char = char
            cur_len = 1
    return max_char, max_len

s = "aabbbccdeeeeee"
char, length = longest_consecutive_char(s)
print(f"最长连续字符: {char}, 长度: {length}")