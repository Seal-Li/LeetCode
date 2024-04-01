def longest_palindrome_subsequence(seq):
    l = 0
    n = len(seq)
    s = ""
    for left in range(n):
        for right in range(left, n):
            sub_seq = seq[left:right+1]
            if sub_seq == sub_seq[::-1] and len(sub_seq) > l:
                l = len(sub_seq)
                s = sub_seq
    return l, s

seq = "abcdefgfedefghijklkjihgfejlsakjdkhljwaihf"
print(longest_palindrome_subsequence(seq))