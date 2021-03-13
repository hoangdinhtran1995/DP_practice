# brute force
def canSum(sum, numbers):
    if sum == 0:
        return True
    if sum < 0:
        return False

    for num in numbers:
        remainder = sum - num
        if canSum(remainder, numbers):
            return True

    return False


def canSum_memo(sum, numbers):
    memo = {}

    def helper(sum, numbers):
        if sum in memo:
            return memo[sum]
        if sum == 0:
            return True
        if sum < 0:
            return False

        for num in numbers:
            remainder = sum - num
            if helper(remainder, numbers):
                memo[sum] = True
                return True

        memo[sum] = False
        return memo[sum]

    return helper(sum, numbers)

def canSum_tab(targ_sum, nums):
    tabl = [False for _ in range(targ_sum+1)]
    tabl[0] = True

    for i in range(targ_sum):
        if tabl[i]:
            for num in nums:
                if i+num <= targ_sum:
                    tabl[i+num] = True

    return tabl[targ_sum]


