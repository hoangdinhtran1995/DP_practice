
def num_ways(data):
    memo = {}

    def helper(data):
        k = len(data)

        if k == 0:
            return 1
        if int(data[0]) == 0:
            return 0
        if k in memo:
            return memo[k]

        result = helper(data[1:])
        if k >= 2 and int(data[:2]) <= 26:
            result += helper(data[2:])

        memo[k] = result
        return result

    return helper(data)