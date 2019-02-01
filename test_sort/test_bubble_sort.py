# 冒泡排序  稳定排序算法
def bubble_sort(nums):
    for i in range(0, nums.__len__()):
        for j in range(0, nums.__len__()-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    list = [45, 32, 8, 33, 12, 22, 19, 97]
    print(bubble_sort(list))
