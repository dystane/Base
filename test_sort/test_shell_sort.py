# 希尔排序 不稳定排序算法
def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            while i >= gap and nums[i] < nums[i - gap]:
                nums[i], nums[i - gap] = nums[i - gap], nums[i]
                i -= gap
            pass
        gap //= 2
        print(nums)
    return nums


if __name__ == '__main__':
    print(shell_sort([45, 32, 8, 33, 12, 22, 19, 97]))
