class Solution:

    def palindromePairs(self, words):

        diction, result = {}, []
        for i in range(len(words)):
            #add all reversed words to dict
            diction[words[i][::-1]] = i
        
        for i in range(len(words)):
            word = words[i]
            #check with empty word for corner case
            if ("" in diction) and\
               (diction[""] != i) and\
               (word == word[::-1]):
                result.append([i, diction[""]])

            for j in range(1, len(word) + 1):
                #left and right for subwords 
                # and words-palindromes in case w1+w2
                # but not w2+w1

                left, right = word[:j], word[j:]

                if (left in diction) and\
                   (diction[left] != i) and\
                   (right == right[::-1]):

                    result.append([i, diction[left]])

                if (right in diction) and\
                   (diction[right] != i) and\
                   (left == left[::-1]):

                    result.append([diction[right], i])

        return result


# Time: O(nk^2)
# n = |{words} 
# k = |{words[i]}|
# Space: O(n)


sol = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(sol.palindromePairs(words))
# [[0, 1], [1, 0], [3, 2], [2, 4]]

words = ["bat","tab","cat"]
print(sol.palindromePairs(words))
# [[0, 1], [1, 0]]

words = ["", "abd", "ba", "db", "hghdba"]
print(sol.palindromePairs(words))
# [[3, 1], [1, 2], [1, 4]]

words = ["", ""]
print(sol.palindromePairs(words))
# [[0, 1]]

words = ["a"]
print(sol.palindromePairs(words))
# []
