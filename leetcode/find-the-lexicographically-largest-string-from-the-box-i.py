class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # adding a char = always larger
        # so word length = always max possible (given lexicographical)
        # i.e. word - numfriends + 1 length
        if numFriends == 1:
            return word
        max_idx = 0
        index = 1
        while index < len(word):
            last_idx = max_idx
            print(f"Last idx {last_idx}, index {index}, and the word {word[last_idx]}")
            last_index = index
            next_index = None
            while index < len(word) and word[index] == word[last_idx]:
                if next_index is None and index > last_index and word[index] >= word[max_idx]:
                    next_index = index
                last_idx += 1
                index += 1
            if index < len(word) and word[index] > word[last_idx]:
                max_idx = last_index # we get a better index!!! yay
                if next_index is None:
                    next_index = index
                # but we also have to process this index
                #index -= 1
            print(f"Index {index}, word")
            index = next_index if next_index and next_index > max_idx else index + 1
        print("max idx", max_idx)
        max_word_len = len(word) - numFriends + 1
        return word[max_idx: min(len(word), max_idx + max_word_len)]