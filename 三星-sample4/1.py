def combination_sum(target, nums):
    def backtrack(start, target, path, result):
        if target == 0:
            result.append(path[:])  # 找到一个组合，加入结果集
            return
        for i in range(start, len(nums)):
            if target - nums[i] >= 0:
                path.append(nums[i])
                backtrack(i, target - nums[i], path, result)
                path.pop()  # 回溯

    result = []
    nums.sort()  # 排序数组，方便剪枝
    backtrack(0, target, [], result)
    return result

# 示例
target_number = 9
number_array = [2, 3, 4, 5]
result_combinations = combination_sum(target_number, number_array)
print(result_combinations)
