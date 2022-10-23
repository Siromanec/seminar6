class Solution:
    def checkSubarraySum(self, numbers, summ_val) -> bool:
        hsmap, cur_summ = {0: 0}, 0
        for i in range(len(numbers)):
            cur_summ += numbers[i]
            if cur_summ % summ_val not in hsmap:
                hsmap[cur_summ % summ_val] = i + 1
            elif hsmap[cur_summ % summ_val] < i:
                return True
        return False

sol = Solution()
nums = [23,2,4,6,7]
k = 6
#start with hash map {0:0}

#when i=0 - num=23:
#  cur sum = 23
#  add to hash map 5:1 (because 23%6 = 5)
#when i=1 - num=2: 
#  cur sum = 25
#  add to hash map 1:2 (because 25%6 = 1 )
#when i=2 - num=4:
#  cur sum = 29
#  29%6 = 5, it is already in hash map -> 
#  hashmap[5] = 1 -> (1 < 2) ->
#  return True


print(sol.checkSubarraySum(nums, k))
#true

nums = [0, 20000000, 34,2]
k = 35
print(sol.checkSubarraySum(nums, k))
#false


#time complexity:
# O(len(numbers)):
# O(len(numbers)) for hsmap
# O(1) - for every element
# 
# we have: sum, hsmap
# iterating over index i (to len(numbers)) 
# adding unexisting hashmap[number[i]] = i
# if we have case with already existing:
# hashmap[number[i]] < i:
# return True
