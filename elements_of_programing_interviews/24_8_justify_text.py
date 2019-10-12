def justify_text(words, L):
    cur_len = 0
    res = []
    cur_line = []
    for word in words:
        if len(word) + len(cur_line) + cur_len > L:  # current word length + existing word length + space length
            for i in range(L - cur_len):
                cur_line[i % max(1, len(cur_line) - 1)] += ' '
            res.append("".join(cur_line))
            # reset
            #             space_len = L - cur_len
            #             if len(cur_line) > 1:
            #                 common_space_len = space_len // (len(cur_line) - 1)
            #                 for i in range(space_len % (len(cur_line) - 1)):
            #                     cur_line[i] += ' '
            #                 res.append((' ' * common_space_len).join(cur_line))
            #             else:
            #                 res.append(cur_line[0].ljust(L))

            cur_line = []
            cur_len = 0
        cur_line.append(word)
        cur_len += len(word)
    if cur_line:
        res.append(' '.join(cur_line).ljust(L))
    return res


if __name__ == '__main__':
    L = 11
    words = ("The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dogs.")
    print(justify_text(words, L))
