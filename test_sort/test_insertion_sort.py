# 插入排序  稳定排序
def insertion_sort(nums):
    for i in range(nums.__len__()):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


if __name__ == '__main__':
    print(insertion_sort([45, 32, 8, 33, 12, 22, 19, 97, 80]))
