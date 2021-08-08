"""
"hello"" world"", abc"" ",
"""

class CVS:

    def encode(self, arr):
        res = []
        for s in arr:
            if '"' in s or ',' in s:
                out = '"' + s.replace('"', '""') + '"'
            else:
                out = s
            res.append(out)
        return ','.join(res)

    # def decode_(self, s, res):
    #     if len(s) == 0:
    #         return
    #
    #     if s[0] == '"':
    #         has_quote = True
    #     else:
    #         has_quote = False
    #
    #     new_st = ''
    #     if not has_quote:
    #         for i, ch in enumerate(s):
    #             if ch != ',':
    #                 new_st += ch
    #                 continue
    #             res.append(new_st)
    #             self.decode_(s[i + 1:], res)
    #             return
    #
    #     two_quotes = True
    #     for i, ch in enumerate(s):
    #         if i == 0:
    #             continue
    #         if ch not in ('"', ','):
    #             new_st += ch
    #             continue
    #         if ch == '"':
    #             if not two_quotes and i > 1 and s[i - 1] == '"':
    #                 two_quotes = True
    #                 continue
    #             new_st += ch
    #             two_quotes = False
    #             continue
    #         if ch == ',':
    #             if two_quotes:
    #                 new_st += ch
    #             else:
    #                 res.append(new_st[:-1])
    #                 self.decode_(s[i + 1:], res)
    #                 return

    # def decode(self, s):
    #     res = []
    #     self.decode_(s, res)
    #     return res

    def decode(self, s):
        is_decode_quote = False
        is_start_quote = False
        is_end_quote = False
        s += ','
        tmp_st = ''
        res = []
        for i, ch in enumerate(s):
            if ch not in ('"', ','):
                tmp_st += ch
                continue
            if ch == '"':
                if not is_start_quote:
                    is_start_quote = True
                    continue
                if not is_decode_quote:
                    if s[i + 1] == '"':
                        is_decode_quote = True
                    else:
                        is_end_quote = True
                    continue
                tmp_st += ch
                is_decode_quote = False
                continue
            if ch == ',':
                if not is_start_quote:
                    res.append(tmp_st)
                    tmp_st = ''
                    continue
                if is_end_quote:
                    res.append(tmp_st)
                    tmp_st = ''
                    is_start_quote = False
                    is_end_quote = False
                    continue
                tmp_st += ch
        return res




if __name__ == '__main__':
    s = 'hello world,"hello, world","hello"" world"""'
    sol = CVS()
    arr = sol.decode(s)
    print(arr)
    print(sol.encode(arr))


    s = '"""hello"",abc"", a",hello world,"abc,abc"'
    arr = sol.decode(s)
    print(arr)
