from typing import List


def binary_search(a: List[int], num: int):
    i = 0
    j = len(a) - 1
    while i <= j:
        mid = (i + j) // 2
        if a[mid] == num:
            return mid
        elif a[mid] > num:
            j = mid - 1
        else:
            i = mid + 1

    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    arr.sort()
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 1) == 1
    assert binary_search(arr, 10) == 10

    assert binary_search(arr, -6) == -1
