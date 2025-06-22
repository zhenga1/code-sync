class Solution:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def decodeString(self, s: str) -> str:
        def stringBuilder(strseg):
            # assumed strseg starts with number k and brackets
            i = 0
            
            while i < len(strseg) and strseg[i] != "[":
                i += 1
            # print(strseg)
            # print(strseg[:i])
            cnt = int(strseg[:i])
            str_repeated = strseg[i+1:-1] # we also don't want the last "]"
            str_actual = ""
            index = 0
            
            while index < len(str_repeated):
                c = str_repeated[index]
                if c in digits:
                    startindex = index
                    while index < len(str_repeated) and str_repeated[index] != '[':
                        index += 1
                    index = index + 1
                    closing = 1
                    while index < len(str_repeated) and closing > 0:
                        if str_repeated[index] == '[':
                            closing += 1
                        if str_repeated[index] == ']':
                            closing -= 1
                        index += 1
                    str_actual += stringBuilder(str_repeated[startindex:index])
                else:
                    str_actual += c
                    index += 1
            lis = [str_actual] * cnt
            return "".join(lis)
        
        startindex = 0
        index = 0
        lis_strs = []
        #print(index)
        while index < len(s):
            if s[index] in digits:
                start_idx = index
                #print(index)
                while index < len(s) and s[index] != '[':
                    index = index + 1
                closing = 1
                index = index + 1
                while index < len(s) and closing > 0:
                    if s[index] == '[':
                        closing += 1
                    if s[index] == ']':
                        closing -= 1
                    index += 1
                print(s[start_idx:index])
                #break
                lis_strs.append(stringBuilder(s[start_idx:index]))
            else:
                lis_strs.append(s[index])
                index += 1
        return "".join(lis_strs)