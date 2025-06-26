class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # i.e. nums[i] - rev(nums[i]) ==  nums[j] - rev(nums[j])
        arr = [x - int(str(x)[::-1]) for x in nums]
        some_dic = {}
        pairs = 0
        MOD = 10**9 + 7
        for x in arr:
            if x in some_dic:
                pairs = (pairs + some_dic[x]) % MOD
                some_dic[x] += 1
            else:
                some_dic[x] = 1
        return pairs