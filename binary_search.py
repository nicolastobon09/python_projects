#!/usr/bin/python3


def binary_search(array, left, right, value):
    """
    function that searches for a value in an array of integers
    """
    if (left <= right):
        mid = (left + right) // 2

        if (array[mid] == value):
            return mid
        elif (array[mid] > value):
            return binary_search(array, left, mid - 1, value)
        else:
            return binary_search(array, mid + 1, right, value)
    return (-1)


if __name__ == "__main__":

    size = int(input('Write a size for your array: '))
    array = [int(input('Write a number: ')) for _ in range(size)]
    value = int(input('Value to search for: '))
    array.sort()

    index = binary_search(array, 0, size - 1, value)

    print(array)
    print(f'Found {value} at index: {index}')
