# 选择排序 不稳定排序
def selection_sort(nums):
    for i in range(nums.__len__() - 1):
        min = nums[i]
        for j in range(i, nums.__len__()):
            if nums[j] < min:
                min = nums[j]
                x = j
        nums[i], nums[x] = nums[x], nums[i]
    return nums


if __name__ == '__main__':
    print(selection_sort([45, 32, 8, 33, 12, 22, 19, 97, 80]))
