
def bestSum(targ_sum, nums):
    if targ_sum == 0: return []
    if targ_sum < 0: return None

    shortest_comb = None

    for num in nums:
        rem = targ_sum - num
        rem_comb = bestSum(rem, nums)
        if rem_comb is not None:
            rem_comb.append(num)
            comb = rem_comb
            # if comb is shorter than shortest, update
            if shortest_comb is None or len(comb) < len(shortest_comb):
                shortest_comb = comb

    return shortest_comb

def bestSum_memo(targ_sum, nums):

    memo = {}

    def helper(targ_sum, nums):
        if targ_sum in memo: return memo[targ_sum]
        if targ_sum == 0: return []
        if targ_sum < 0: return None

        shortest_comb = None

        for num in nums:
            rem = targ_sum - num
            rem_comb = helper(rem, nums)
            if rem_comb is not None:
                rem_comb = rem_comb + [num]
                # if comb is shorter than shortest, update
                if shortest_comb is None or len(rem_comb) < len(shortest_comb):
                    shortest_comb = rem_comb

        memo[targ_sum] = shortest_comb
        return memo[targ_sum]

    return helper(targ_sum,nums)

def bestSum_tab(targ_sum, nums):
    tabl = [None for _ in range(targ_sum+1)]
    tabl[0] = []

    for i in range(targ_sum):
        if tabl[i] is not None:
            for num in nums:
                if i + num <= targ_sum:
                    new_candidate = tabl[i] + [num]
                    if tabl[i+num] is None or len(new_candidate) < len(tabl[i + num]):
                        tabl[i + num] = new_candidate
    return tabl[-1]
