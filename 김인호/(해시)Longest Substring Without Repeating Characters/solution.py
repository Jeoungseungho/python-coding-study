class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        # i 는 길이를 세기 시작하는 시작하는 idx
        i = 0
        ans = 0
        char_dict = {}

        for j in range(len(s)):
            # 현재 문자인 s[j]가 이미 dict에 있고
            # 현재 문자와 같은 문자인 char_dict[s[j]]가 i보다 크거나 같으면
            # i를 char_dict[s[j]] 보다 1 큰수로 하여 중복을 없앤 범위로 갱신한다.
            # 그렇지 않은 경우(중복이 없는 경우), ans를 갱신한다.
            if s[j] in char_dict and i <= char_dict[s[j]]:
                i = char_dict[s[j]] + 1
            else:
                ans = max(ans, j - i + 1)

            char_dict[s[j]] = j

        return ans
