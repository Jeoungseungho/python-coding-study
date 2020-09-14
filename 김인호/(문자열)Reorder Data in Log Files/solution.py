class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        s, d = [], []
        ans = []
        for l in logs:
            i = 0
            while i < len(l) and l[i] != " ":
                i += 1
            identifier = l[:i]
            letter = l[i + 1 :]
            if letter[0].isalpha():
                s.append((letter, l))
            else:
                d.append(l)

        s.sort()

        for _, l in s:
            ans.append(l)

        ans.extend(d)

        return ans

# 다른 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        s, d = [], []
        ans = []
        for l in logs:
            temp = l.split()
            if temp[1].isalpha():
                s.append(l.split(maxsplit=1))
            else:
                d.append(l)

        s = sorted(sorted(s, key=lambda x: x[0]), key=lambda x: x[1])

        for i in s:
            ans.append(" ".join(i))

        for i in d:
            ans.append(i)

        return ans
