
def howSum(targ_sum, nums):
    if targ_sum == 0: return []
    if targ_sum < 0: return None

    for num in nums:
        rem = targ_sum - num
        rem_res = howSum(rem, nums)
        if rem_res is not None:
            rem_res.append(num)
            return rem_res

    # if not possible to rem_res to 0
    return None

def howSum_memo(targ_sum, nums):
    memo = {}

    def helper(targ_sum, nums):
        # base cases and memo case
        if targ_sum in memo: return memo[targ_sum]
        if targ_sum == 0: return []
        if targ_sum < 0: return None

        for num in nums:
            rem = targ_sum - num
            rem_res = helper(rem, nums)
            if rem_res is not None:
                rem_res.append(num)
                memo[targ_sum] = rem_res
                return memo[targ_sum]

        # if not possible to rem_res to 0
        memo[targ_sum] = None
        return memo[targ_sum]

    return helper(targ_sum,nums)

def howSum_tab(targ_sum, nums):
    tabl = [None for _ in range(targ_sum+1)]
    tabl[0] = []

    for i in range(targ_sum):
        if tabl[i] is not None:
            for num in nums:
                if i+num <= targ_sum:
                    tabl[i+num] = tabl[i] + [num]
    return tabl[-1]
