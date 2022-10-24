from math import inf

class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""

        Dict = {}
        for char in t:
            if char not in Dict:
                Dict[char] = 1
            else:
                Dict[char] += 1

        num_of_ch, counter = len(Dict), 0
        #counter for characters that are in t but not in s

        left, right = 0, 0
        result, shortest= '', inf

        while right < len(s):
            if s[right] in Dict:
                Dict[s[right]] -= 1
                if Dict[s[right]] == 0:
                    counter += 1
                    

            while left <= right and\
                  counter == num_of_ch:
                lenn = right + 1 - left

                if lenn < shortest:
                    result = s[left:right+1]
                    shortest = lenn

                if s[left] in Dict:
                    Dict[s[left]] += 1
                    if Dict[s[left]] == 1:
                        counter -= 1

                left += 1          
            right += 1
        return result


#time O(len(s))
#space: O(len(t))



sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s, t))
#"BANC"

s = "A"
t = "ABC"
print(sol.minWindow(s, t))
# ""

s = "gsc"
t = "gc"
print(sol.minWindow(s, t))
# gsc
