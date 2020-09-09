#모범답안


class Solution:
    def lengthOfLongestSubstring(self, s):
        arr = {}
        start = 0
        length = 0

        for index, char in enumerate(s):
            if char in arr and start <= arr[char]:
                start = arr[char] + 1
            else:
                length = max(length, index - start + 1)

            arr[char] = index

        return length


s1 = Solution()

print(s1.lengthOfLongestSubstring('abcdae'))
