class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=lambda x: len(x))
        used_words = {}
        max_len = 0
        for word in words:
            if word not in used_words:
                used_words[word] = 1
                for i in range(len(word)):
                    sub_word = word[:i] + word[(i + 1):]
                    if sub_word in used_words:
                        used_words[word] = max(used_words[word], 1 + used_words[sub_word])
            max_len = max(max_len, used_words[word])
        return max_len
