def validation(arr, target):
    if not (2 <= len(arr) <= 3 * 10**4):
        raise IndexError('list out of range')

    for i in arr:
        if not (-1000 <= i <= 1000):
            raise ValueError('number out of range')
            break

    if not (-2000 <= target <= 2000):
        raise ValueError('sum of 2 numbers is out of range')


def target_elements(arr, target):
    validation(arr, target)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i + 1, j + 1
    return "can't find the numbers"

arr = [-8, -3, 1, 2, 3, 5, 12, 23]
target = 0

print(target_elements(arr, target))