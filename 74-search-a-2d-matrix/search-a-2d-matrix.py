def bs(array, target):
    left = 0
    right = len(array) - 1

    while left<=right:
        mid = left + (right-left) // 2
        print(f'mid:{mid} . arr[mid]:{array[mid]}')
        if array[mid] == target:
            print("??")
            return True
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        # # else:
        # elif array[mid] == target:
        #     return True

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if bs(matrix[i], target):
                return True
        return False